'''
Asal : 
salam ostad vaght bekheyr dar file core.py line208 , 209 ye moshkeli hast ke run nemishe mige
return outside function mn garchi aghab jelo mikonm dorost nemishe


APM: 
salam ,  baratoon eslah krdm va neveshtamesh.
mitoonid kole code ro bebarid editor ya IDE khdoeton
oonja rahat tare kar krdn bad inja copy paste konid
baz soali bood beporsid moafagh bashid

Asal:
ostad be nazare shoma man kare digeii ham bayad anjam bedam ya bayad sabr
koniam ta jalase 2 ?


APM:
salam aya porozheye shoma takmil shode? tashih beshe?
'''
from database import get_session
from utils import hash_password, check_password
from models import Customer, Account , Transaction
import numpy as np
from datetime import datetime



class AdminPanel:
    def __init__(self):
        self.session=get_session()


    def create_customer(self,name,last_name,email,phone,address):
        #row tooye database besazam
        
        #^^^
        #kare shomast *** age, phone, address tooye models.py inja ham bezarid *******
        customer= Customer(name=name,last_name = last_name,email=email,phone = phone , address = address)

        #ta alan classesho sakhti tooye python
        #zakhire bshe?? tooey db
        self.session.add(customer)
        self.session.commit()
        print(f'customer {name} created successfully')
        return customer

    def create_account(self,customer_id,account_type,balance, pin):
        customer=self.session.get(Customer,customer_id)
        #row ro bekesham biron

        if not customer:
            
            raise Exception(f'Customer with id {customer_id} not found')
        #1) hash pin
        hashed_pin=hash_password(pin)

        #lag banki
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(
            f"[BANK SYSTEM]\n"
            f"Time: {timestamp}\n"
            f"Customer ID: {customer_id}\n"
            f"Status: Verified ✓\n"
            f"Action: Generating new card number..."
           )

        #2) sakht shomare card
        card_number = self._generate_card_number()

        #3) sakht hesab
        account = Account(
            customer_id=customer_id,
            account_type=account_type,
            balance=balance,
            pin=pin,
            card_number=card_number
        )


        #4) zakhire
        self.session.add(account)
        self.session.commit()

        # 5) chap natije
        print(f"Account created for customer {customer_id} | Card Number: {card_number}")

        return account


    #-------

    def show_balance(self,account_id):
        account=self.session.get(Account,account_id)
        if not account:
            print(f"[BAKN SYSTEM] : Balance cheak faild-> account {account_id}: not found.")

            raise Exception(f'Account with id {account_id} not found')

        balance= account.balance

        print (f"Account {account_id} | Current balance: {balance}")
        return balance

    
    def deposit(self,account_id,amount):
        account=self.session.get(Account,account_id)
        if not account:
            print (f" [BANK SYSTEM] Deposit failed -> Account {account_id} not found ")
            raise Exception(f'Account with id {account_id} not found')
        
        # variz movafagh
        old_balance = account.balance
        account.balance = old_balance + amount
        self.session.commit()

        print(
            f"[BANK SYSTEM] Deposit successful \n"
            f"Account: {account_id}\n"
            f"Old Balance: {old_balance:,.0f} USD\n"
            f"Amount Deposited: {amount:,.0f} USD\n"
            f"New Balance: {account.balance:,.0f} USD"
    )

        return account

    def withdraw(self,account_id,amount):
        account = self.session.get(Account , account_id)

        if not account:
            print(f"[BANK SYSTEM]: Withdrawal failed → Account {account_id} not found ")
            raise Exception(f"Account with id {account_id} not found")
    
        # mojodi ghabl
        old_balance = account.balance

        #cheeck kardan mojodi

        if amount > old_balance:
            print(
                f"[BANK SYSTAM]: Withdraw denied."
                f"Account:{account_id} USD \n"
                f"Attempted:{amount:,.0f} USD \n"
                f"Available: {old_balance:,.0f} USD\n"
                f"Reason: Insufficient funds"
            )
            raise Exception("Insufficient balance")

        account.balance -= amount
        self.session.commit()

        print(
            f"[BANK SYSTEM] Withdrawal successful ✓\n"
            f"Account: {account_id}\n"
            f"Old Balance: {old_balance:,.0f} USD\n"
            f"Amount Withdrawn: {amount:,.0f} USD\n"
            f"New Balance: {account.balance:,.0f} USD"
    )

        return account



    def transfer(self,from_account_id,to_account_id,amount):
        #daryaft hesab
        from_acc = self.session.get(Account , from_account_id)
        to_acc = self.session.get(Account , to_account_id)

        #cheak hesab ferestande
        if not from_acc:
            print(f"Transfer faild -> sender account {from_account_id} not found.")
            raise Exception(f"sender account with ID {from_account_id} not found.")
        
        #cheak hesab girandeh
        if not to_acc:
            print(f"Transfer faild -> Receiver account {to_account_id} not found.")
            raise Exception(f"Receiver account with ID  {to_account_id} not found.")

        #cheak mojodi 
        if amount > from_acc.balance:
            print(
                f"[BANK SYSTEM] Transfer denied X \n"
                f"From Account :{from_account_id}\n"
                f"To Account : {to_account_id}\n"
                f"Atempted Amount: {amount:,.0f} USD \n"
                f"Availble Balance : {from_acc.balance:,.0f} USD \n"
                f"Reason: Insufficient funds"
            )
            raise Exception("Insufficient balance")
        
        #bardasht az ferestande
        old_from_balance = from_acc.balance
        from_acc.balance -= amount

        #variz be girande
        old_to_balance = to_acc.balance
        to_acc.balance += amount

        self.session.commit()

        #last print
        print(
            f"[BANK SYSTEM] Transfer Successful \n"
            f"From Account :{from_account_id}\n"
            f"To Account: {to_account_id}\n"
            f"Anount :{amount:,.0f} USD\n"
            f"Sender OLD balance:{old_from_balance:,.0f} USD\n"
            f"Sender NEW balance :{from_acc.balance:,.0f} USD\n"
            f"Resiver OLD balance:{old_to_balance:,.0f} USD\n"
            f"Receiver NEW balance:{to_acc.balance:,.0f} USD\n"
        )
        return from_acc, to_acc



    def show_transaction(self,account_id):
        #cheak kardan account
        account = self.session.get(Account , account_id)
        if not account:
            print(f" [BANK SYSTEM]: Transactions failed -> Account {account_id} not found. X")
            raise Exception(f"Account with id {account_id} not found")
        
        #gereftan trakonesh ha
        transactions = (
        self.session
        .query(Transaction)
        .filter_by(account_id=account_id)
        .order_by(Transaction.time.desc())
        .all()
    )
        if not transactions:
            print(f"[BAMK SYSTEM]: NO Transaction found for account : {account_id}")
            return []
        
        #prin bank
        print(f"[BANK SYSTEM]: Transaction history for account {account_id}: ")
        print("-" *60 )
        
        for i in transactions:
            sign = "+" if i.type == "deposit" else "-"
            time_str = i.time.strftime("%Y-%m-%d %H:%M:%S")
            print(
            f"{time_str} | {i.type.upper():8} | {sign}{i.amount:,.0f} USD")
            
            print("-" * 60)

        return transactions


    


    #shomare card
    def _generate_card_number(self):
        return ''.join(np.random.randint(0, 10, 16).astype(str))
    


    






#class GUI --> 
#gui --> fucntion --> adminpanel.create() adminpanel.() felan felan()\

#a=AdminPanel()
#a.create_customer('ali','email' , 'password', 'sen','shomare carte melisho bege')







