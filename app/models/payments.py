from .base import Base
from sqlalchemy import String, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import date, time, datetime


if TYPE_CHECKING:
    from .users import Students
    from .courses import Courses




class Payments(Base):
    __tablename__ = "payments"


    txn_id : Mapped[str] = mapped_column(String(50), primary_key=True)
    student_id : Mapped[int] = mapped_column(ForeignKey("students.student_id"))
    service : Mapped[str] = mapped_column(String(50), nullable=False)
    service_id : Mapped[int] = mapped_column(ForeignKey("courses.course_id"))
    txn_date : Mapped[date] = mapped_column(Date, default=date.today())
    txn_time : Mapped[time] = mapped_column(Time, default=lambda: datetime.now().time())
    method : Mapped[str] = mapped_column(String(50), nullable=False)
    amount : Mapped[int] = mapped_column(Integer, nullable=False)

    course : Mapped["Courses"] = relationship(back_populates="transaction")
    student : Mapped["Students"] = relationship(back_populates="transaction")