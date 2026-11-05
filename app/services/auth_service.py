from app.repos import UserRepo, StudentRepo
import bcrypt
from app.database import logger
from app.exceptions import NotFoundError, InvalidCerdiantialsError, UnexpectedErrorAccuerd
from datetime import datetime, timedelta, timezone
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

class Authentication:
    def __init__(self, db):
        self.db = db
        self.user_db = UserRepo(db)
        self.students_db = StudentRepo(db)
        self.__secret_key = os.getenv("SECRET_KEY")
        self.__algoritham = os.getenv("ALGORITHAM")
        

    def SignIn(self, username : str, password : str) -> object:
        try:
            username = str(username)
            password = str(password)

            user_data = self.user_db.get_user(username)
            if not user_data:
                raise InvalidCerdiantialsError("Invalid Username OR Password")
            hashed_password = user_data.password

            if not bcrypt.checkpw(password.encode(), hashed_password.encode("utf-8")):
                raise InvalidCerdiantialsError("Invalid Username Or Password")
            else:
                return user_data
                

        except (TypeError, ValueError):
            logger.exception("Password Verification Failed")
            raise
    
    

    def SignUp(self, username: str, mobile_no : str, email : str, name : str, city : str, password : str) -> object:
        try:
            username = str(username)
            check_username = self.user_db.get_user(username)
            if check_username:
                raise InvalidCerdiantialsError("Username Already Exists")
            mobile_no = str(mobile_no)
            email = str(email)
            check_student = self.students_db.check_student(mobile_no, email)
            if check_student:
                raise InvalidCerdiantialsError("Mobile Number Or Email Already Exists")
            name = str(name)
            city = str(city)
            password = str(password)

            hasheded_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()

            new_user = self.user_db.add_user(
                username=username,
                password=hasheded_password,
            )

            if not new_user:
                raise UnexpectedErrorAccuerd("Unexpected Error While Creating New User")
            new_student = self.students_db.add_student(
                user_id=new_user.user_id,
                name=name,
                mobile_no=mobile_no,
                email=email,
                city=city
            )
            if not new_student:
                delete_user = self.user_db.delete_user(new_user.username)
                raise UnexpectedErrorAccuerd("Unexpected Error While Creating New Student")

            return new_user
        except (TypeError, ValueError):
            logger.exception("User Creation failed")
            raise

    def reset_password(self, username : str, old_password : str, new_password : str) -> object:
        user_data = self.user_db.get_user(username)
        if not user_data:
            raise NotFoundError("User Not Found")

        hashed_pasword = user_data.password
        if not bcrypt.checkpw(old_password.encode(), hashed_pasword.encode("utf-8")):
            InvalidCerdiantialsError("Invalid Password")

        new_hashed = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode()

        update_password = self.user_db.update_user_data(username, "password", new_hashed)
        if not update_password:
            raise UnexpectedErrorAccuerd("Error While Updating Your Password")
        return update_password



    def create_token(self, user : object):
        student = user.student
        payload = {
        "sub" : "Student Data",
        "user_id" : user.user_id,
        "username" : user.username,
        "student_id" : student.student_id,
        "role" : user.role,
        "exp" : datetime.now(timezone.utc) + timedelta(minutes=10)
        }

        token = jwt.encode(
            payload,
            self.__secret_key,
            self.__algoritham            
        )    
        return token
    
    def verify_token(self, token):
        payload = jwt.decode(
            token,
            self.__secret_key,
            self.__algoritham
        )

        return payload


    