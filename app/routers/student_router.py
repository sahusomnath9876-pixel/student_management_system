from fastapi import APIRouter, Depends
from app.database import get_db
from app.exceptions import InvalidCerdiantialsError
from app.services import StudentService, CourseService
from app.schemas import Enroll, EnrollResponse, AddCourse, CourseDetails, StudentData, UpdateStudent
from .auth_router import verify_token




def role_check(role : str):
    def check_role(current_user : dict = Depends(verify_token)):
        current_role = current_user.get("role")

        if role.lower() != current_role.lower():
            raise InvalidCerdiantialsError("You Are Not Allowed To Perform This Operation")
        return current_user
    return check_role


student_router = APIRouter(prefix=("/students"), tags=["student_services"], dependencies=[Depends(role_check("student"))])




@student_router.post("/enroll", response_model=EnrollResponse)
def enroll_in_course(course : Enroll, db=Depends(get_db), student_data = Depends(verify_token)):
    student_id = student_data.get("student_id")
    student = StudentService(db, student_id)
    enroll = student.enroll_in_course(course.course_id, course.method, course.cerdentials)

    return enroll


@student_router.get("/search", response_model=CourseDetails)
def search_for_course(search_keyword : str, db=Depends(get_db), student_data=Depends(role_check("student"))):
    student_id = student_data.get("student_id")
    student = StudentService(db, student_id)

    search = student.search_courses(search_keyword)

    for course_data in search:
        return course_data


@student_router.get("/courses", response_model=list[CourseDetails])
def get_all_courses(db=Depends(get_db)):
    course = CourseService(db)

    course_data = course.get_courses()
    return course_data


@student_router.get("/student_data", response_model=StudentData)
def get_student(db=Depends(get_db), current_student=Depends(role_check("student"))):
    student = StudentService(db, current_student["student_id"])

    student_data = student.get_student_data()
    return student_data


@student_router.patch("/update", response_model=StudentData)
def upadate_student(details : UpdateStudent, db=Depends(get_db), current_student=Depends(role_check("student"))):
    student = StudentService(db, current_student["student_id"])

    update = student.update_student(current_student["username"], details.update_type, details.new_data, details.password)
    return update

