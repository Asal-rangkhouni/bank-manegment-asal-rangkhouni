from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

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
    name = Column(String, nullable=False)
    last_name = Column(String)   
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    address = Column(String)
    age = Column(Integer)

    accounts = relationship("Account", back_populates="customer")



#-------Accounts------
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    balance= Column(Float, default=0.0) #mojodi , 00
    account_type = Column(String, default="standard") 
    pin = Column(String, nullable=False) #pin kodom account ro khod kon
    customer_id= Column(Integer, ForeignKey("customers.id"))
    card_number = Column(String, unique=True)
    
    #-------relationships-----
    customer= relationship("Customer", back_populates="accounts")
    transactions= relationship("Transaction", back_populates="account")


#-------Transactions------
class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer , primary_key= True)
    account_id = Column(Integer , ForeignKey("accounts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)

    account = relationship("Account", back_populates="transactions")
