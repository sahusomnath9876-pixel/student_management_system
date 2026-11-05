from app.database import logger
from app.models import Payments
from typing import Any
from sqlalchemy import select




class PaymentRepo:
    def __init__(self, db):
        self.__db = db
        self.__payment = Payments


    def get_payment(self, student_id : int) -> object:
        stmt = select(self.__payment).where(self.__payment.student_id == student_id)
        payment_data = self.__db.scalars(stmt).first()
        if payment_data:
            return payment_data

    def add_payment(self, **kwargs : Any) -> object | None:
        try:
            new_payment = self.__payment(**kwargs)
            self.__db.add(new_payment)
            self.__db.commit()
            self.__db.refresh(new_payment)
            return new_payment
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Creating New payment")
            raise

    def update_payment_data(self, txn_id : str, column_name : str, new_data : Any) -> object:
        try:
            column_name = str(column_name.lower())
            payment_data = self.get_payment(txn_id)
            if payment_data:
                setattr(payment_data, column_name, new_data)
                self.__db.commit()
                self.__db.refresh(payment_data)
                return payment_data
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Updating payment Informations")
            raise


    def delete_payment(self, txn_id : str) -> str:
        try:
            payment_data = self.get_payment(txn_id)
            if payment_data:
                self.__db.delete(payment_data)
                self.__db.commit()
                return txn_id
        except Exception:
            self.__db.rollback()
            logger.exception("Database Error While Deleting the payment")
            raise

