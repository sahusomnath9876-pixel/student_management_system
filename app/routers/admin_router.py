from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.services import CourseService
from app.schemas import AddCourse, CourseDetails, UpdateCourse
from app.repos import UserRepo
from .auth_router import verify_token
from .student_router import role_check

admin_router = APIRouter(prefix="/admin", tags=["Admin"], dependencies=[Depends(role_check("Admin"))])


@admin_router.post("/add_course", response_model=CourseDetails, status_code=201)
def add_new_course(new_course : AddCourse, db=Depends(get_db) ):
    course = CourseService(db)

    add_course = course.add_new_course(
        new_course.course_name, new_course.price, new_course.duration, new_course.total_seates, new_course.en_start,
        new_course.en_end
    )

    return add_course


@admin_router.patch("/update_course")
def update_course(update : UpdateCourse, db=Depends(get_db)):
    course = CourseService(db)

    course_update = course.update_course(update.course_id, update.update_type, update.update_data)
    return{
        "course_id" : course_update,
        "updated_type" : update.update_type,
    }

@admin_router.delete("/delete_course")
def delete_course(course_id : int, db=Depends(get_db)):
    course = CourseService(db)

    delete = course.delete_course(course_id)
    return{
        "detail" : f"Course Id {delete} deleted Successfuly"
    }