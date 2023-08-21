import json 
from datetime import datetime, date
import pytest

from mortgage_app.api import utils

def test_latest_payment_made(test_app, monkeypatch):
    test_data = {
        "created": date(2022, 12, 30),
        "principal": 49911536.33, 
        "interest": 623894.2, 
        "principal_interest": 50535430.53,
        "balance": 49465930.53,
         "monthly_replaymnent": 1069500.0
        }

    async def mock_get_latest(): 
        return test_data
    
    monkeypatch.setattr(utils, "get_latest", mock_get_latest)

    response = test_app.get("/mortgage/latest")
    assert response.status_code == 200
    assert response.json() == test_data


def test_payment_made_by_date(test_app, monkeypatch):

    test_data = {
        "created": date(2022, 12, 30),
        "principal": 49911536.33, 
        "interest": 623894.2, 
        "principal_interest": 50535430.53,
        "balance": 49465930.53,
         "monthly_replaymnent": 1069500.0
        }
    
    async def mock_get_by_date(created): 
        return test_data
    
    monkeypatch.setattr(utils, "get_latest", mock_get_by_date)

    response = test_app.get("/mortgage/2020-12-30/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_payment_made_by_date_incorrectly(test_app, monkeypatch):
    async def mock_get_date(created): 
        return None
    
    monkeypatch.setattr(utils, "get_by_date", mock_get_date)


    response = test_app.get("/mortgage/2020-12-30/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Payment with created 2020-12-30 not found"



def test_remove_payment(test_app, monkeypatch):
    test_data = {
        "created": date(2022, 12, 30),
        "principal": 49911536.33, 
        "interest": 623894.2, 
        "principal_interest": 50535430.53,
        "balance": 49465930.53,
         "monthly_replaymnent": 1069500.0
        }

    async def mock_get_by_date(created): 
        return test_data
    
    monkeypatch.setattr(utils, "get_latest", mock_get_by_date)

    async def mock_delete(created):
        return created
    
    monkeypatch.setattr(utils, "delete", mock_delete)

    response = test_app.get("/mortgage/2020-12-30/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_payment_incorrectly(test_app, monkeypatch):
    async def mock_get_date(created): 
        return None
    
    monkeypatch.setattr(utils, "get_by_date", mock_get_date)


    response = test_app.delete("/mortgage/2020-12-30/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Payment with created 2020-12-30 not found"