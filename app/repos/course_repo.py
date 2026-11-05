from app.models import Courses, EnrolledStudents
from app.database import logger
from typing import Any
from sqlalchemy import select


class CourseRepo:
    def __init__(self, db):
        self.__db = db
        self.__course = Courses

    def search_course(self, search_pattern : str) -> object:
        search_pattern = f"%{search_pattern}%"
        stmt = select(self.__course).where(self.__course.course_name.like(search_pattern))
        course_data = self.__db.scalars(stmt).all()
        if course_data:
            return course_data


    def get_course(self, course_id : int) -> object:
        course_data = self.__db.get(self.__course, course_id)
        if course_data:
            return course_data

    def add_course(self, **kwargs : Any) -> object | None:
        try:
            new_course = self.__course(**kwargs)
            self.__db.add(new_course)
            self.__db.commit()
            self.__db.refresh(new_course)
            return new_course
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Creating New course")
            raise

    def update_course_data(self, course_id : int, column_name : str, new_data : Any) -> object:
        try:
            column_name = str(column_name.lower())
            course_data = self.get_course(course_id)
            if course_data:
                setattr(course_data, column_name, new_data)
                self.__db.commit()
                self.__db.refresh(course_data)
                return course_data
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Updating course Informations")
            raise


    def delete_course(self, course_id : int) -> str:
        try:
            course_data = self.get_course(course_id)
            if course_data:
                self.__db.delete(course_data)
                self.__db.commit()
                return course_id
                
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Deleting the course")
            raise


    def get_all_courses(self):
        stmt = select(self.__course)
        course_data = self.__db.scalars(stmt).all()
        if course_data:
            return course_data


class EnrollmentRepo:
    def __init__(self, db):
        self.__db = db
        self.__enrollment = EnrolledStudents


    def get_enrollment(self, enm_id : int) -> object:
        enrolled_data = self.__db.get(self.__enrollment, enm_id)
        if enrolled_data:
            return enrolled_data

    def add_enrollment(self, **kwargs : Any) -> object | None:
        try:
            new_enrollment = self.__enrollment(**kwargs)
            self.__db.add(new_enrollment)
            self.__db.commit()
            self.__db.refresh(new_enrollment)
            return new_enrollment
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Creating New enrollment")
            raise

    def update_enrollment_data(self, enm_id : int, column_name : str, new_data : Any) -> object:
        try:
            column_name = str(column_name.lower())
            enrolled_data = self.get_enrollment(enm_id)
            if enrolled_data:
                setattr(enrolled_data, column_name, new_data)
                self.__db.commit()
                self.__db.refresh(enrolled_data)
                return enrolled_data
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Updating enrollment Informations")
            raise


    def delete_enrollment(self, enm_id : int) -> str:
        try:
            enrolled_data = self.get_enrollment(enm_id)
            if enrolled_data:
                self.__db.delete(enrolled_data)
                self.__db.commit()
                
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Deleting the enrollment")
            raise