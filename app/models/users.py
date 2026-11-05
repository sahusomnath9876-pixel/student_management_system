from .base import Base
from sqlalchemy import String, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import date, time, datetime


if TYPE_CHECKING:
    from .courses import EnrolledStudents
    from .payments import Payments



class Users(Base):
    __tablename__ = "users"

    user_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username : Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password : Mapped[str] = mapped_column(String(200), nullable=False)
    reg_date : Mapped[date] = mapped_column(Date, default=date.today())
    reg_time : Mapped[time] = mapped_column(Time, default=lambda: datetime.now().time())
    role : Mapped[str] = mapped_column(String(50), nullable=False, default="student")

    student : Mapped["Students"] = relationship(back_populates="user")




class Students(Base):
    __tablename__ = "students"

    student_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    name : Mapped[str] = mapped_column(String(50), nullable=False)
    mobile_no : Mapped[str] = mapped_column(String(50), nullable=False)
    email : Mapped[str] = mapped_column(String(50), nullable=False)
    city : Mapped[str] = mapped_column(String(50), default="Not Added")

    user : Mapped["Users"] = relationship(back_populates="student")
    enrollments : Mapped[list["EnrolledStudents"]] = relationship(back_populates="student")
    transaction : Mapped["Payments"] = relationship(back_populates="student")


# class Admin(Base):
#     __tablename__ = "admins"

#     admin_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
#     name : Mapped[str] = mapped_column(String(50), nullable=False)
#     mobile_no : Mapped[str] = mapped_column(String(50), nullable=False)