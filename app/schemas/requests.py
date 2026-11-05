from pydantic import BaseModel
from datetime import date
from typing import Any

class AuthLogin(BaseModel):
    username : str
    password : str


class AuthReg(BaseModel):
    username : str
    mobile_no : str
    name : str
    email : str
    city : str
    password : str


class CardPayment(BaseModel):
    method : str
    card_no : str
    cvv : str

class UpiPayment(BaseModel):
    course_id : int
    method : str
    upi_id : str

class AddCourse(BaseModel):
    course_name : str
    price : int
    duration : str
    total_seates : int
    en_start : date
    en_end : date

class UpdateCourse(BaseModel):
    course_id : int
    update_type : str
    new_dat : Any


class Enroll(BaseModel):
    course_id : int
    method : str
    cerdentials : str

class UpdateCourse(BaseModel):
    course_id : int
    update_type : str
    update_data : Any
    
class UpdatePassword(BaseModel):
    username : str
    old_password : str
    new_password : str

class UpdateStudent(BaseModel):
    password : str
    update_type : str
    new_data : str