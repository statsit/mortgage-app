from dotenv import dotenv_values
from datetime import datetime


from mortgage_app import __version__

from mortgage_app.app import Mortgage

env = dotenv_values("mortgage_app/.env")
current_month = "2021-04-30"
amount = 2300.00
table_name = 'mortgage_tbl'


mortgage= Mortgage(table_name, env)


def test_date_detect():
    created_date = datetime.strptime(current_month, '%Y-%m-%d')
    assert mortgage.detect_date(created_date) == True

def test_retrieve_balance():
    assert mortgage.retrieve_balance() > 50000000.00
    # print(res)
    # assert len(res) >1

# def test_monthly_payment():
#     res = mortgage.monthly_payment(current_month, amount)
#     assert res['monthly_replayment'] > 0
#     assert res['balance'] > 0
#     assert res['monthly_payment_AUD'] > 0
#     assert res['interest'] > 0
#     assert res['principal_interest'] > 0

def test_version():
    assert __version__ == '0.1.0'
