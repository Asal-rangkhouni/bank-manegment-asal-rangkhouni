'''
Class --> vasl bshe b sootone databaset

'''


from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base



#--------------------TABLE K MIKHAY BSAZI CLASS------


#_----costumer table------
''''

------customers---------------
id name      email       password   card_number      accounts
1   ali    ali@gmail.com   123456    23282717231       accoutn(details....)
2   reza   reza@gmail.com  123456                   [4,5]


---account------
id balance type pin ..   card_number

'''


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    email= Column(String, unique=True)
    age = Column(Integer)
    phone = Column(String)
    address = Column(String)

    accounts= relationship("Account", back_populates="customer")




#-------Accounts------
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    balance= Column(Float, default=0.0) #mojodi , 00
    type = Column(String, default="standard") # 'standard', 'foreign', 'crypto'
    pin = Column(String, nullable=False) #pin kodom account ro khod kon
    customer_id= Column(Integer, ForeignKey("customers.id"))
    
    #-------relationships-----
    customer= relationship("Customer", back_populates="accounts")
    transactions= relationship("Transaction", back_populates="account")



#-------Transactions------
class Transaction(Base):
    __tablename__ = "Transaction"
    id = Column(Integer , primary_key= True)
    account_id = Column(Integer , ForeignKey = ("accounts.id"))
    amount = Column(Float)
    type = Column(String)
    time = Column(DateTime, default=datetime.utcnow)