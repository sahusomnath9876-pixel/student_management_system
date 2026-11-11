from .base import Base
from sqlalchemy import String, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import date, time, datetime


if TYPE_CHECKING:
    from .users import Students
    from .payments import Payments



class Courses(Base):
    __tablename__ = "courses"

    course_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_name : Mapped[str] = mapped_column(String(50), nullable=False)
    price : Mapped[int] = mapped_column(Integer, nullable=False)
    course_duration : Mapped[str] = mapped_column(String(50), nullable=False)
    total_seates : Mapped[int] = mapped_column(Integer, nullable=False)
    total_enrolled : Mapped[int] = mapped_column(Integer, default=0)
    en_start : Mapped[date] = mapped_column(Date, nullable=False)
    en_end : Mapped[date] = mapped_column(Date, nullable=False)


    enrollments : Mapped[list["EnrolledStudents"]] = relationship(back_populates="course")
    transaction : Mapped["Payments"] = relationship(back_populates="course")


class EnrolledStudents(Base):
    __tablename__ = "enrolled_students"

    enm_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id : Mapped[int] = mapped_column(ForeignKey("courses.course_id"))
    student_id : Mapped[int] = mapped_column(ForeignKey("students.student_id"))
    enm_date : Mapped[date] = mapped_column(Date, default=date.today())
    enm_time : Mapped[time] = mapped_column(Time, default=lambda: datetime.now().time())
    txn_id : Mapped[str] = mapped_column(ForeignKey("payments.txn_id"))


    course : Mapped["Courses"] = relationship(back_populates="enrollments")
    student : Mapped["Students"] = relationship(back_populates="enrollments")
    

    