from dataclasses import dataclass 
import os
from datetime import date, timedelta
from dotenv import dotenv_values
import dataset

PRINCIPAL = 54500000
RATE = 0.15
EXCHANGE_RATE = 465


class Connection: 
    def __init__(self,  env:dict) -> None:
        """
        Create connection to database
        """
        self.host=env['POSTGRES_HOST']
        self.dbname=env['POSTGRES_DB']
        self.user=env['POSTGRES_USER']
        self.password=env['POSTGRES_PASSWORD']
        self.port=env['POSTGRES_PORT']


    def print_connection_string(self) -> None:
        """
        Print connection string
        """
        # print(self.env)
        print(f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}')
        
   
    def connect(self) -> dataset.Database:
        """
        Connect to database
        """
        db = dataset.connect(f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}')
        return db

class Mortgage(Connection):
    
    """
    Mortgage class for calculating monthly mortgage payments
    """
    def __init__(self, table_name:str, env: str=dotenv_values('.env')):
        # self.month = last_month
        self.table_name = table_name
        self.principal= PRINCIPAL
        self.monthly_repayment= 0
        self.balance= PRINCIPAL
        self.interest_rate= RATE
        self.exchange_rate= EXCHANGE_RATE
        super().__init__(env)
   

    def monthly_payment(self,current_month:date, amount:float, monthly_payment:float=None) -> float:
        """
        Calculate monthly mortgage payment in Naira and generate a dictionary of the result
        Args:
            current_month (date): current month
            amount (float): amount in AUD
            monthly_payment (float): monthly payment in Naira. It is defaulted to None
        Returns:
            dictionary of created date, principal, interest, principal_interest, balance, monthly_repayment, monthly_repayment_AUD
        """
        if self.retrieve_balance() is not None:
            self.principal = self.retrieve_balance()
        
        self.monthly_repayment = amount * self.exchange_rate

        if monthly_payment is not None:
            self.monthly_repayment = monthly_payment

        self.monthly_payment_AUD = amount
        self.monthly_interest = (self.principal * self.interest_rate ) / 12
        self.principal_interest = self.monthly_interest + self.principal
        self.balance = self.principal_interest - self.monthly_repayment
        return {
            'created': current_month, 
             'principal': self.principal, 
             'interest': round(self.monthly_interest, 2), 
             'principal_interest': round(self.principal_interest, 2), 
             'balance': round(self.balance,2),
             'monthly_repayment': self.monthly_repayment,
             'monthly_repayment_AUD': amount
             }

    def detect_date(self, created_date:date) -> bool:
        """
        Detect if created date is less than current date
        Args:
            created_date (date): created date
        Returns:
            bool

        """
        today_month = date.today().month
        today_year = date.today().year

        if created_date.year == today_year and created_date.month < today_month:
            return True
        if created_date.year < today_year and created_date.month > today_month:
            return True
       
        return False



    def retrieve_balance(self) -> float:
        """
        Return last balance from database

        Returns:
            float
        """
        db = super().connect()
        # result = db[self.table_name].find_one(created=self.month)

        result = db.query(f"SELECT * FROM {self.table_name} ORDER BY created DESC LIMIT 1")

        for row in result:

        # if result is  None:
        #     return None
        # else:
            if self.detect_date(row['created'])==True:
            # if row['balance'] is not None:
                    return row['balance']
            return None


    def insert_result(self, current_month:date, amount:float, monthly_payment=None) -> None:
        """
        Insert result into database
        Args:
            current_month (date): current month
            amount (float): amount in AUD
        Returns:
            None
        """
        with super().connect() as db:
            if monthly_payment is not None:
                db[self.table_name].insert(self.monthly_payment(current_month, amount, monthly_payment))
            else:
                db[self.table_name].insert(self.monthly_payment(current_month, amount))
        


