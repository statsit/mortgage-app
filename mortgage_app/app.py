from dataclasses import dataclass 
import os
from dotenv import dotenv_values
import dataset

PRINCIPAL = 54500000
RATE = 0.15


class Connection: 
    def __init__(self, env: str=dotenv_values('.env')) -> None:
        """
        Create connection to database
        """
       
        self.host=env['POSTGRES_HOST']
        self.dbname=env['POSTGRES_DB']
        self.user=env['POSTGRES_USER']
        self.password=env['POSTGRES_PASSWORD']
        self.port=env['POSTGRES_PORT']
        
   
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
    def __init__(self, last_month):
        self.month = last_month
        self.principal= PRINCIPAL
        self.monthly_replayment= 0
        self.balance= PRINCIPAL
        self.interest_rate= RATE
        super().__init__(self)
   

    def monthly_payment(self,current_month, amount:float) -> float:
        """
        Calculate monthly mortgage payment
        """
        if self.retrieve_balance is not None:
            self.principal = self.retrieve_balance
        self.monthly_replayment = amount
        self.monthly_interest = (self.principal * self.interest_rate ) / 12
        self.principal_interest = self.monthly_interest + self.principal
        self.balance = self.principal_interest - self. monthly_replayment
        return {
            'month': current_month, 
             'principal': self.principal, 
             'interest': self.monthly_interest, 
             'principal_interest': self.principal_interest, 
             'balance': self.balance
             }


    def retrive_balance(self, ) -> float:
        """
        Return balance
        """
        db = super().connect()
        result = db['mortgage'].find_one(month=self.month)
        return result['balance']


    def insert_result(self, current_month, amount) -> None:
        """
        Insert result into database
        """
        with super().connect() as db:
             db['mortgage'].insert(self.monthly_payment(current_month, amount))
        


