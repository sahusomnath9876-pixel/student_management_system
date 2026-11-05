from pydantic import BaseModel, ConfigDict
from datetime import date

class SignUpResponse(BaseModel):
    username : str
    user_id : int
  

    model_config = ConfigDict(from_attributes=True)
class EnrollResponse(BaseModel):
    enm_id : int
    course_id : int
    student_id : int
    txn_id : str
    model_config = ConfigDict(from_attributes=True)


class CourseDetails(BaseModel):
    course_id : int
    course_name : str
    price : int
    course_duration : str
    en_start : date
    en_end : date

    model_config = ConfigDict(from_attributes=True)



class StudentData(BaseModel):
    student_id : int
    name : str
    mobile_no : str
    email : str
    city : str

    model_config = ConfigDict(from_attributes=True)