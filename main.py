from datetime import datetime
from  fire import Fire

from mortgage_app.app import Mortgage 


last_month="2020-01-01"
current_month = "2020-02-01"
amount = 700000

def main(amount, last_month, current_month):
    last_month = datetime.strptime(last_month, 2020-02-01'%Y-%m-%d')
    current_month = datetime.strptime(current_month, '%Y-%m-%d')
    amount = float(amount)
    mortgage= Mortgage(last_month)
    mortgage.insert_result(current_month, amount)


if __name__ == '__main__':
    Fire(main)