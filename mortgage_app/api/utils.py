from datetime import datetime, date 

from mortgage_app.api.models import MortgageSchema, RepaymentSchema
from mortgage_app.db import mortgage_tbl, database


async def post(payload: RepaymentSchema):
    """
    Make payment to the mortgage
    Args:
        payload (RepaymentSchema): The payment details
    
    """
    result = await get_latest()
    if result.balance is not None:
        principal = result.balance
        
    monthly_repayment = payload.amount * payload.exchange_rate

    # monthly_payment_AUD = payload.amount
    monthly_interest = (principal * payload.interest_rate ) / 12
    principal_interest = monthly_interest + principal
    balance = principal_interest - monthly_repayment

    query = mortgage_tbl.insert().values(
        principal=principal, 
        interest=round(monthly_interest, 2), 
        principal_interest=round(principal_interest, 2), 
        balance=round(balance,2),
        monthly_repayment=monthly_repayment,
        monthly_repayment_aud= payload.amount,
        exchange_rate=payload.exchange_rate,
        interest_rate=payload.interest_rate
    )
    return await database.execute(query=query)


async def get_all():
    """Get all the payments made to the mortgage

    Returns:
        list: A list of all the payments made to the mortgage
    """
    query = mortgage_tbl.select()
    return await database.fetch_all(query=query)


async def get_latest():
    """Get the last payment made to the mortgage
    
    Returns:
        dict: The last payment made to the mortgage
    """
    query = "SELECT * FROM mortgage_tbl ORDER BY created DESC LIMIT 1"
    return await database.fetch_one(query=query)

async def get_by_date(created: str):
    """Get a payment made to the mortgage by date
    Args:
        created (str): The date the mortgage was created

    Returns:
        dict: The payment made to the mortgage by date
    """
    query = f"SELECT * FROM mortgage_tbl WHERE created = '{created}'"
    # query = test_mortgage_tbl.select().where(test_mortgage_tbl.c.created == created)
    return await database.fetch_one(query=query)

async def put(created: str, payload: MortgageSchema):
    """Update the mortgage table with the new values
    Args:
        created (str): The date the mortgage was created
        payload (MortgageSchema): The new values to update the mortgage table with
    Returns:
        [type]: [description]
    """
    created = datetime.strptime(created, "%Y-%m-%d").date()
    query = (
        mortgage_tbl.update()
        .where(created == mortgage_tbl.c.created)
        .values(principal=payload.principal, interest=payload.interest, principal_interest=payload.principal_interest, balance=payload.balance)
        .returning(mortgage_tbl.c.created)
    )
    return await database.execute(query=query)

async def delete(created: str):
    """Delete a payment made to the mortgage by date
    Args:
        created (str): The date the mortgage was created
    Returns:
        [type]: [description]
    """
    created = datetime.strptime(created, "%Y-%m-%d").date()
    query = mortgage_tbl.delete().where(mortgage_tbl.c.created == created)
    return await database.execute(query=query)

async def get_last_rows(row_num):
    """Get the last rows from the mortgage table
    Args:
        row_num (int): The number of rows to return
    Returns:
        list: A list of the last rows from the mortgage table
    """
    query = f"SELECT * FROM mortgage_tbl ORDER BY created DESC LIMIT {row_num}"
    return await database.fetch_all(query=query)



