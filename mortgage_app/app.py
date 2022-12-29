from dataclasses import dataclass 
import os
from datetime import date, timedelta
from dotenv import dotenv_values
import dataset

PRINCIPAL = 54500000
RATE = 0.15


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
    def __init__(self, table_name, env: str=dotenv_values('.env')):
        # self.month = last_month
        self.table_name = table_name
        self.principal= PRINCIPAL
        self.monthly_replayment= 0
        self.balance= PRINCIPAL
        self.interest_rate= RATE
        super().__init__(env)
   

    def monthly_payment(self,current_month, amount:float) -> float:
        """
        Calculate monthly mortgage payment
        """
        if self.retrieve_balance() is not None:
            self.principal = self.retrieve_balance()
        self.monthly_replayment = amount
        self.monthly_interest = (self.principal * self.interest_rate ) / 12
        self.principal_interest = self.monthly_interest + self.principal
        self.balance = self.principal_interest - self. monthly_replayment
        return {
            'created': current_month, 
             'principal': self.principal, 
             'interest': round(self.monthly_interest, 2), 
             'principal_interest': round(self.principal_interest, 2), 
             'balance': round(self.balance,2),
             'monthly_replayment': amount
             }

    def detect_date(self, created_date:date) -> bool:
        """
        Detect date
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
        Return balance
        """
        db = super().connect()
        # result = db[self.table_name].find_one(created=self.month)

        result = db.query(f"SELECT * FROM {self.table_name} ORDER BY created DESC LIMIT 1")

        for row in result:

        # if result is  None:
        #     return None
        # else:
            if self.detect_date(row['created'])==True:
                    return row['balance']
            return None


    def insert_result(self, current_month, amount) -> None:
        """
        Insert result into database
        """
        with super().connect() as db:
             db[self.table_name].insert(self.monthly_payment(current_month, amount))
        


