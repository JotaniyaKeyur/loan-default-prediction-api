from pydantic import BaseModel, Field, computed_field
from typing import Annotated

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Prediction input with computed fields
class PredictionInput(BaseModel):

    RevolvingUtilizationOfUnsecuredLines: Annotated[float, Field(..., ge=0, le=50708, description="Ratio of credit card and personal credit line balances to total credit limit.")]
    age: Annotated[int, Field(..., ge=0, le=109, description="Age of the individual in years.")]
    NumberOfTime30_59DaysPastDueNotWorse: Annotated[int, Field(..., ge=0, le=98, description="Number of times payment was 30–59 days past due but not worse.")]
    DebtRatio: Annotated[float, Field(..., ge=0, le=329664, description="Monthly debt payments, alimony, and living costs divided by monthly gross income.")]
    MonthlyIncome: Annotated[float, Field(..., ge=0, le=3008750, description="Monthly income of the individual.")]
    NumberOfOpenCreditLinesAndLoans: Annotated[int, Field(..., ge=0, le=58, description="Number of open loans and credit lines.")]
    NumberOfTimes90DaysLate: Annotated[int, Field(..., ge=0, le=98, description="Number of times payment was 90 days or more past due.")]
    NumberRealEstateLoansOrLines: Annotated[int, Field(..., ge=0, le=54, description="Number of real estate loans or mortgage accounts.")]
    NumberOfTime60_89DaysPastDueNotWorse: Annotated[int, Field(..., ge=0, le=98, description="Number of times payment was 60–89 days past due but not worse.")]
    NumberOfDependents: Annotated[float, Field(..., ge=0, le=20, description="Number of dependents in the household.")]

    @computed_field
    @property
    def TotalPastDue(self) -> float:
        return (self.NumberOfTime30_59DaysPastDueNotWorse + self.NumberOfTime60_89DaysPastDueNotWorse + self.NumberOfTimes90DaysLate)

    @computed_field
    @property
    def DebtRatioPerDependent(self) -> float:
        return self.DebtRatio / (self.NumberOfDependents + 1)

    @computed_field
    @property
    def UtilizationPerLine(self) -> float:
        return self.RevolvingUtilizationOfUnsecuredLines / (self.NumberOfOpenCreditLinesAndLoans + 1)

    @computed_field
    @property
    def IncomeDebtRatio(self) -> float:
        return self.MonthlyIncome / (self.DebtRatio + 1)

    @computed_field
    @property
    def HasDependents(self) -> int:
        return int(self.NumberOfDependents > 0)

    @computed_field
    @property
    def HighDebtRatio(self) -> int:
        return int(self.DebtRatio > 1)

    @computed_field
    @property
    def HighUtilization(self) -> int:
        return int(self.RevolvingUtilizationOfUnsecuredLines > 0.8)

class PredictionOut(BaseModel):
    predicted_category: int
