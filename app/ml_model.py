import pickle
import pandas as pd
from .schemas import PredictionInput

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(data: PredictionInput) -> int:
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
