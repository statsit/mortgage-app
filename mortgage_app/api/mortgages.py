from typing import List
from datetime import datetime
from fastapi import APIRouter, HTTPException

from mortgage_app.api import utils
from mortgage_app.api.models import MortgageSchema, RepaymentSchema, RepaymentDB

router = APIRouter()

@router.post("/", response_model=RepaymentDB, status_code=201)
async def make_payment(payload: RepaymentSchema):
    mortgage = await utils.get_latest()
    if mortgage is None:
       raise HTTPException(status_code=404, detail="Mortgage not found")

    mortgage_id = await utils.post(payload)

    response_object = {
        "created": datetime.now(),
        "amount": payload.amount,
        "exchange_rate": payload.exchange_rate,
        "interest_rate": payload.interest_rate
    }

    return response_object

@router.get("/", response_model=List[MortgageSchema])
async def read_all_payments():
    return await utils.get_all()

@router.get("/latest", response_model=MortgageSchema)
async def read_single_payment():
    return await utils.get_latest()

@router.get("/{row_id}/", response_model=List[MortgageSchema])
async def read_last_rows_mortgage(row_id: int):
    return await utils.get_last_rows(row_id)


@router.get("/get_by_date", response_model=MortgageSchema)
async def read_payment_by_date(created:str):
    mortgage = await utils.get_by_date(created)
    if not mortgage:
        raise HTTPException(status_code=404, detail="Payment with created {created} not found")

    return mortgage


@router.put("/{created}/", response_model=MortgageSchema)
async def update_payment(created: datetime, payload: MortgageSchema):
    mortgage = await utils.get_by_date(created)
    if not mortgage:
        raise HTTPException(status_code=404, detail="Payment with created {created} not found")

    mortgage_id = await utils.put(created, payload)

    response_object = {
        "created": created,
        "principal": payload.principal,
        "interest": payload.interest,
        "principal_interest": payload.principal_interest,
        "balance": payload.balance
    }

    return response_object


@router.delete("/{created}/")
async def delete_payment(created: str):
    mortgage = await utils.get_by_date(created)
    if not mortgage:
        raise HTTPException(status_code=404, detail=f"Payment with created {created} not found")

    await utils.delete(created)

    return {"detail": "Payment deleted successfully"}




    
