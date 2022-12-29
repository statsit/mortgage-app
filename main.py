from datetime import datetime
from  fire import Fire
from dotenv import dotenv_values

from mortgage_app.app import Mortgage, Connection


current_month = "2022-12-30"
amount_in_aus = 2300
rate_in_naira = 465
amount = float(amount_in_aus * rate_in_naira)
table_name = 'test_mortgage_tbl'
env = dotenv_values("mortgage_app/.env")

def main(
    amount=amount, 
    current_month=current_month, 
    table_name='test_mortgage_tbl'
    ):
    current_month = datetime.strptime(current_month, '%Y-%m-%d')
    amount = float(amount)
    mortgage= Mortgage(table_name, dotenv_values("mortgage_app/.env"))
    mortgage.insert_result(current_month, amount)
    print(f'{amount} for {current_month} has been paid')


if __name__ == '__main__':
    Fire(main)    