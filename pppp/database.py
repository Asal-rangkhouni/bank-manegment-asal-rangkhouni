'''
Connect mikone databse ro b SQLALCHEMY 
ma fght inja tarif mikonim k b kodom database vasl beshe
tamame code hameja hamine

har projecti

'''


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

#--> SQLALCHEMY --> DATABASE NISTA --> vasete beyne python database

'''
hard --> PostgreSQL , SQLite , MySQL ,....

memory --> Redis 

'''

#mysql , ....
DATABASE_URL = "sqlite:///database.db"

engine= create_engine("mysql+mysqlconnector://asal:Milad004800@localhost",echo=False, future=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine , autoflash=False, autocommit=False,future=True )


#helper

def get_session():
    return SessionLocal()
