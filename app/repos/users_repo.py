from app.models import Users, Students
from sqlalchemy import select, or_
from typing import Any
from app.database import logger


class UserRepo:
    def __init__(self, db):
        self.__db = db
        self.__users = Users


    def get_user(self, username : str) -> object:
        stmt = select(self.__users).where(self.__users.username == username)
        user_data = self.__db.scalars(stmt).first()
        if user_data:
            return user_data

    def add_user(self, **kwargs : Any) -> object | None:
        try:
            new_user = self.__users(**kwargs)
            self.__db.add(new_user)
            self.__db.commit()
            self.__db.refresh(new_user)
            return new_user
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Creating New User")
            raise

    def update_user_data(self, username : str, column_name : str, new_data : Any) -> object:
        try:
            column_name = str(column_name.lower())
            user_data = self.get_user(username)
            if user_data:
                setattr(user_data, column_name, new_data)
                self.__db.commit()
                self.__db.refresh(user_data)
                return user_data
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Updating User Informations")
            raise


    def delete_user(self, username : str) -> str:
        try:
            user_data = self.get_user(username)
            if user_data:
                self.__db.delete(user_data)
                self.__db.commit()
                return username
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Deleting the User")
            raise






class StudentRepo:
    def __init__(self, db):
        self.__db = db
        self.__student = Students


    def get_student(self, student_id : int) -> object:
        student_data = self.__db.get(self.__student, student_id)
        if student_data:
            return student_data

    def check_student(self, mobile_no : str, email : str) -> object | None:
        stmt = select(self.__student).where(or_(self.__student.mobile_no == mobile_no, self.__student.email == email))
        student_data = self.__db.scalars(stmt).first()
        if student_data:
            return student_data

    def add_student(self, **kwargs : Any) -> object | None:
        try:
            new_student = self.__student(**kwargs)
            self.__db.add(new_student)
            self.__db.commit()
            self.__db.refresh(new_student)
            return new_student
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Creating New student")
            raise

    def update_student_data(self, student_id : int, column_name : str, new_data : Any) -> object:
        try:
            column_name = str(column_name.lower())
            student_data = self.get_student(student_id)
            if student_data:
                setattr(student_data, column_name, new_data)
                self.__db.commit()
                self.__db.refresh(student_data)
                return student_data
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Updating student Informations")
            raise


    def delete_student(self, student_id : int) -> str:
        try:
            student_data = self.get_student(student_id)
            if student_data:
                self.__db.delete(student_data)
                self.__db.commit()
                return student_id
                
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Deleting the student")
            raise



    
       
        

