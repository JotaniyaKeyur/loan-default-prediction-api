import pandas as pd
from xgboost import XGBClassifier
import os
from .schemas import PredictionInput

# Absolute path to model.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model.json")

model = XGBClassifier()
model.load_model(MODEL_PATH)

def predict(data: PredictionInput) -> int:
    # Convert Pydantic model (with computed fields) to dict
    data_dict = {
        "RevolvingUtilizationOfUnsecuredLines" : data.RevolvingUtilizationOfUnsecuredLines,
         "age" : data.age,
         "NumberOfTime30-59DaysPastDueNotWorse" : data.NumberOfTime30_59DaysPastDueNotWorse,
         "DebtRatio" : data.DebtRatio,
         "MonthlyIncome" : data.MonthlyIncome,
         "NumberOfOpenCreditLinesAndLoans" : data.NumberOfOpenCreditLinesAndLoans,
         "NumberOfTimes90DaysLate" : data.NumberOfTimes90DaysLate,
         "NumberRealEstateLoansOrLines" : data.NumberRealEstateLoansOrLines,
         "NumberOfTime60-89DaysPastDueNotWorse" : data.NumberOfTime60_89DaysPastDueNotWorse,
         "NumberOfDependents" : data.NumberOfDependents,
         "TotalPastDue" : data.TotalPastDue,
         "DebtRatioPerDependent" : data.DebtRatioPerDependent,
         "UtilizationPerLine" : data.UtilizationPerLine,
         "IncomeDebtRatio" : data.IncomeDebtRatio,
         "HasDependents" : data.HasDependents,
         "HighDebtRatio" : data.HighDebtRatio,
         "HighUtilization" : data.HighUtilization
    }

    df = pd.DataFrame([data_dict])
    prediction = int(model.predict(df)[0])
    return prediction
