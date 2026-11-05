from app.repos import PaymentRepo
from app.exceptions import *
from datetime import datetime
from app.database import logger



class PaymentService:
    def __init__(self, db):
        self.db = db
        self.payments_db = PaymentRepo(db)

    def __generate_transaction_id(self) -> str:
        now = datetime.now()

        letters = "TXN"
        date_time = now.strftime("%Y%m%d%H%M%S%f")
        txn_id = letters + date_time
        return txn_id

    def make_new_transaction(self, student_id : int, service_name : str, service_id : int, method : str, amount : int) -> object:
        try:
            student_id = int(student_id)
            service_name = str(service_name)
            service_id = int(service_id)
            method = str(method)
            txn_id = self.__generate_transaction_id()

            new_transaction = self.payments_db.add_payment(
                txn_id=txn_id,
                student_id=student_id,
                service=service_name,
                service_id=service_id,
                method=method,
                amount=amount
            )
            if not new_transaction:
                raise UnexpectedErrorAccuerd("Transaction Failed Due To Unexpected Error")
            return new_transaction
        except (TypeError, ValueError):
            logger.exception("Transaction Failed")
            raise