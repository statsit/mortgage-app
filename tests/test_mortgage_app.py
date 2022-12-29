from dotenv import dotenv_values
from datetime import datetime


from mortgage_app import __version__

from mortgage_app.app import Mortgage

env = dotenv_values("mortgage_app/.env")
current_month = "2022-08-30"
amount = 700000.00
table_name = 'test_mortgage_tbl'


mortgage= Mortgage( table_name, env)


def test_date_detect():
    created_date = datetime.strptime(current_month, '%Y-%m-%d')
    assert mortgage.detect_date(created_date) == True

def test_retrieve_balance():
    assert mortgage.retrieve_balance() > 50000000.00
    # print(res)
    # assert len(res) >1

def test_version():
    assert __version__ == '0.1.0'
