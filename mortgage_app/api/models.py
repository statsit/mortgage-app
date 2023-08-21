from pydantic import BaseModel
from datetime import datetime, date

class MortgageSchema(BaseModel):
    created: date
    principal: float
    interest: float
    principal_interest: float
    balance: float
    monthly_repayment: float
    monthly_repayment_aud: float
    exchange_rate: int
    interest_rate: float

class RepaymentSchema(BaseModel):
    amount: float
    exchange_rate: int = 465
    interest_rate: float = 0.15


class RepaymentDB(RepaymentSchema):
    created: datetime