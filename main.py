from fastapi import FastAPI
import joblib
import uvicorn
from pydantic import BaseModel

diabetes_app = FastAPI()

model = joblib.load('model_diabetes.pkl')
scaler = joblib.load('scaler_diabetes.pkl')

class DiabetesFeatures(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@diabetes_app.post('/predict')
async def predict_diabetes(diabetes: DiabetesFeatures):
    features = [[
        diabetes.Pregnancies,
        diabetes.Glucose,
        diabetes.BloodPressure,
        diabetes.SkinThickness,
        diabetes.Insulin,
        diabetes.BMI,
        diabetes.DiabetesPedigreeFunction,
        diabetes.Age
    ]]

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    probability = model.predict_proba(features_scaled)

    return {
        "diabetes": bool(prediction[0]),
        "probability": round(float(probability[0][1]), 2)
    }

if __name__ == '__main__':
    uvicorn.run(diabetes_app, host='127.0.0.1', port=9000)