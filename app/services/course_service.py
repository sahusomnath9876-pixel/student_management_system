from app.database import logger
from app.exceptions import *
from app.repos import CourseRepo, EnrollmentRepo
from datetime import date
from typing import Any




class CourseService:
    def __init__(self, db):
        self.db = db
        self.course_db = CourseRepo(db)


    def add_new_course(self, course_name : str, price : int, duration : str, total_seates : int, en_start : date, en_date : date) -> object:
        try:
            course_name=str(course_name)
            price=int(price)
            duration=str(duration)
            total_seates=int(total_seates)
            strat_date = en_start
            end_date = en_date

            new_course = self.course_db.add_course(
                course_name=course_name,
                price=price,
                course_duration=duration,
                total_seates=total_seates,
                en_start=strat_date,
                en_end=end_date
            )

            if not new_course:
                raise UnexpectedErrorAccuerd("Course Craetion Failed")
            return new_course
        except (TypeError, ValueError):
            logger.exception("Unable to add this course at this moment")
            raise

    def update_course(self, course_id : int, update_type : str, new_data : Any) -> object:
        course_date = self.course_db.get_course(course_id)
        if not course_date:
            raise NotFoundError("Course Not Founded")

        update_type = str(update_type)
        update = self.course_db.update_course_data(course_id, update_type, new_data)

        if not update:
            raise UnexpectedErrorAccuerd("Unable To Upate this Course")
        return update

    def delete_course(self, course_id : int):
        course_data = self.course_db.get_course(course_id)
        if not course_data:
            raise NotFoundError("Course Not Founded")
        delet_course = self.course_db.delete_course(course_id)
        if not delet_course:
            raise UnexpectedErrorAccuerd("Course Deletation Failed")
        return delet_course



    def get_courses(self):
        course_data = self.course_db.get_all_courses()
        if not course_data:
            raise NotFoundError("Course Data Not Founded")
        return course_data


    def view_enrolled_students(self, course_id : int) -> list[object]:
        course = self.course_db.get_course(course_id)
        enrollment = course.enrollments
        return enrollment