from datetime import datetime
from  fire import Fire
from dotenv import dotenv_values

from mortgage_app.app import Mortgage, Connection


last_month="2020-01-01"
current_month = "2020-02-01"
amount = 700000.00
table_name = 'mortgage_tbl'
env = dotenv_values("mortgage_app/.env")

def main(
    amount, 
    last_month, 
    current_month, 
    table_name='test_mortgage_tbl'
    ):
    last_month = datetime.strptime(last_month, '%Y-%m-%d')
    current_month = datetime.strptime(current_month, '%Y-%m-%d')
    amount = float(amount)
    mortgage= Mortgage(last_month, table_name, dotenv_values("mortgage_app/.env"))
    mortgage.insert_result(current_month, amount)
    print(f'{amount} for {current_month} has been paid')


if __name__ == '__main__':
    # conn = Connection(last_month, table_name, dotenv_values("mortgage_app/.env"))
    # mortgage= Mortgage(last_month, table_name, env)
    # conn.print_connection_string()
    # mortgage.print_connection_string()
    Fire(main)    