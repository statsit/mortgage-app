from datetime import datetime, date
from  fire import Fire
from dotenv import dotenv_values

from mortgage_app.app import Mortgage, Connection


current_month = date.today().strftime('%Y-%m-%d')
amount = 2300.00
# monthly_payment = 0 #700000
table_name = 'mortgage_tbl'
env = dotenv_values("mortgage_app/.env")

def main(
    amount=amount, 
    current_month=current_month, 
    table_name=table_name,
    # monthly_payment=monthly_payment
    )-> None:
    """
    Main function that calls the Mortgage class and insert the result into the database
    Args:
        amount (float): amount in AUD
        current_month (date): current month
        table_name (str): table name
    """
    current_month = datetime.strptime(current_month, '%Y-%m-%d')
    amount = float(amount)
    # monthly_payment = float(monthly_payment)
    mortgage= Mortgage(table_name, dotenv_values("mortgage_app/.env"))
    mortgage.insert_result(current_month, amount) #monthly_payment)
    print(f'{amount} for {current_month} has been paid')


if __name__ == '__main__':
    Fire(main)   
    