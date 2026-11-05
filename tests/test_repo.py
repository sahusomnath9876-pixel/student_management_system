from app.repos import UserRepo, StudentRepo
from app.database import SessionLocal

db = SessionLocal()

def test_user_crud():
    user = UserRepo(db)

#     new_user = user.add_user(
#         username="somnath29s",
#         password="Sahu@2956",
#         role="Customer"
#     )

#     assert new_user.username == "somnath29s"

    user_data = user.get_user("somnath29s")
    assert user_data.password == "Sahu@2956"
    update_user = user.update_user_data("somnath29s", "Password", "Sahu@2020")
    assert update_user.username == "somnath29s"
   


def test_student_crud():
    student = StudentRepo(db)

    # new_student = student.add_student(
    #     user_id=18998,
    #     name="Somnath Sahu",
    #     mobile_no="758996969",
    #     email="example@gmail.com",
    #     city="Baharagora"
    # )
    # assert new_student.user_id == 18998

    student_data = student.get_student(145263)
    assert student_data.city == "Baharagora"
    update_data = student.update_student_data(student_data.student_id, "Email", "Sahu@email.com")

    assert update_data.email == "Sahu@email.com"

    