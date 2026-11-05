import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

def db_engine():
    load_dotenv()

    host=os.getenv("db_host")
    user=os.getenv("db_user")
    database=os.getenv("db_database")
    password=os.getenv("db_password")
    driver=os.getenv("driver_name")

    url = f"{driver}://{user}:{password}@{host}/{database}"

    engine = create_engine(url)
    return engine

