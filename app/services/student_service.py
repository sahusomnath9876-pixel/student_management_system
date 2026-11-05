from app.repos import CourseRepo, EnrollmentRepo, PaymentRepo, UserRepo, StudentRepo
from app.database import logger
from app.exceptions import UnexpectedErrorAccuerd, NotFoundError, InvalidCerdiantialsError
from app.exceptions import CourseFullOrExpierdError, PaymentFailedError
from datetime import date
from .payment_service import PaymentService
from typing import Any
from .auth_service import Authentication



class StudentService:
    def __init__(self, db, student_id):
        self.db = db
        self.student_id = student_id
        self.user_db = UserRepo(db)
        self.student_db = StudentRepo(db)
        self.course_db = CourseRepo(db)
        self.enrollment_db = EnrollmentRepo(db)
        self.pay_service = PaymentService(db)
        self.pay_repo =PaymentRepo(db)
        self.auth = Authentication(db)


    def search_courses(self, search_pattern : str) -> object:
        search_result = self.course_db.search_course(search_pattern)
        if not search_result:
            raise NotFoundError("Course not founded try again")
        return search_result

    #currently for learning we are using dummy payment system
    def pay_method(self, method : str, cerdintials : str ):
        supported_methods = ["CARD", "UPI"]
        if method.upper() not in supported_methods:
            raise PaymentFailedError("Unsupported Method")
        if method.upper() == "CARD":
            card_no = cerdintials
            if len(card_no) != 16:
                raise PaymentFailedError("Invalid Card Number")
            return method
        elif method.upper() == "UPI":
            upi_id = cerdintials
            if upi_id:
                return method


    def check_course(self, course_id : int)-> object:
        course_data = self.course_db.get_course(course_id)
        if not course_data:
            raise NotFoundError("Course Not Founded")
        today = date.today()
        if course_data.en_start > today:
            raise CourseFullOrExpierdError("Course Enrollment hasn't started yrt..")
        if course_data.en_end < today:
            raise CourseFullOrExpierdError("Enrollment date has expierd")
        if course_data.total_enrolled >= course_data.total_seates:
            raise CourseFullOrExpierdError("Seates Are Fulled Sorry")
        return course_data

    def enroll_in_course(self, course_id : int, method : str, cerdiantials : str) -> object:
        
        course_data = self.check_course(course_id)
        payment = self.pay_method(method, cerdiantials)
        if not payment:
            raise PaymentFailedError("Payment Failed")
        make_payment = self.pay_service.make_new_transaction(self.student_id, "Course", course_data.course_id, payment, course_data.price)
        if not payment:
            raise PaymentFailedError("Payment Failed Error")
        new_enroll = self.enrollment_db.add_enrollment(
            course_id = course_data.course_id,
            student_id=self.student_id,
            txn_id=make_payment.txn_id
        )
        if not new_enroll:
            delete_txn = self.pay_repo.delete_payment(make_payment.txn_id)
            raise UnexpectedErrorAccuerd("Course Enrollment Failed")
        total_enrolled = course_data.total_enrolled + 1
        update_seates = self.course_db.update_course_data(course_data.course_id, "total_enrolled", total_enrolled)
        if not update_seates:
            logger.debug("Seates Updation Failed")

        return new_enroll
    
    def get_student_data(self) -> object:
        student_data = self.student_db.get_student(self.student_id)
        if not student_data:
            raise NotFoundError("Student Not Exists")
        return student_data
        
        
    def update_student(self, username : str, update_type : str, new_data : str, password : str) -> object:
        verify_student = self.auth.SignIn(username, password)
        if not verify_student:
            raise InvalidCerdiantialsError("Invalid Password")  
        update = self.student_db.update_student_data(self.student_id, update_type, new_data)
        if not update:
            raise UnexpectedErrorAccuerd("Unable To Update Your Details")
        return update
    

