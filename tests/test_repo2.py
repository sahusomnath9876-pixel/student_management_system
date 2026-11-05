from app.repos import PaymentRepo, CourseRepo, EnrollmentRepo
from app.database import SessionLocal



db = SessionLocal()

















def test_course_repo():
    course = CourseRepo(db)

    add_course = course.add_course(
        course_name="Data Science",
        price=7850,
        course_duration="6 Months",
        total_seates=785,
        en_start='2026-11-19',
        en_end='2026-11-29'

    )
    assert add_course.course_name == "Data Science"

    get_course = course.get_course(add_course.course_id)
    assert get_course.course_id == add_course.course_id
    update_course = course.update_course_data(get_course.course_id, "price", 9999)
    assert update_course.price == 9999

    transaction = PaymentRepo(db)

    add_pay = transaction.add_payment(
        txn_id="TXN2345555",
        student_id=145263,
        service="Course",
        service_id=get_course.course_id,
        method="UPI"
    )

    assert add_pay.student_id == 145263
    get_pay = transaction.get_payment(145263)
    assert get_pay.method == "UPI"
    update_txn = transaction.update_payment_data(add_pay.txn_id, "method", "Card")
    assert update_txn.method == "Card"

    enroll = EnrollmentRepo(db)

    add_enroll = enroll.add_enrollment(
        course_id=78597,
        student_id=145263,
        txn_id="TXN2345555",            
    )

    assert add_enroll.course_id == 78597
    get_enroll = enroll.get_enrollment(add_enroll.enm_id)
    assert get_enroll.enm_id == add_enroll.enm_id
    update_enroll = enroll.update_enrollment_data(get_enroll.enm_id)
    assert update_enroll == get_enroll.enm_id
   


