from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL = "mysql+mysqlconnector://asal:Milad004800@localhost/your_db_name"

engine= create_engine(DATABASE_URL, echo=False, future=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

#helper
def get_session():
    return SessionLocal()
