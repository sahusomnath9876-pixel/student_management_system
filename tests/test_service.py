from app.services import Authentication
from app.services import StudentService
from app.services import PaymentService, CourseService
from app.database import SessionLocal

db = SessionLocal()

# def test_auth():
#     auth = Authentication(db)

#     new_user = auth.SignUp("somnath29s", "7859652632", "sahu980@gamil.com", "Somnath Sahu", "Baharagora", "Sahu@2020")
#     assert new_user.username == "somnath29s"

#     login = auth.SignIn("somnath29s", "Sahu@2020")
#     assert login.username == "somnath29s"

def test_course():
    # course = CourseService(db)

    # add_course = course.add_new_course(
    #     "Python 2.0", 999, "6 Months", 900, "2026-11-24", "2027-01-01"
    # )
    # assert add_course.price == 999

    # update = course.update_course(add_course.course_id, "price", 780)
    # assert update.price == 780


    # student = StudentService(db, 145263)

    # enroll_course = student.enroll_in_course(78596)
    # assert enroll_course.student_id == 145263

    course = CourseService(db)

    enrollment = course.view_enrolled_students(78596)
    assert enrollment.enm_id == 2563223
