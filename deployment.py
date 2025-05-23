from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")


model = joblib.load(r"C:\Users\nice\Desktop\sales-forecasting-project (1)\sales-forecasting-project\models\xgb_model.pkl")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("template.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def post_predict(
    request: Request,
    Inventory_Level: float = Form(...),
    Demand_Forecast: float = Form(...),
    Holiday_Promotion: int = Form(...),
    month: int = Form(...),
    Rolling_Mean_7: float = Form(...),
    Rolling_Std_7: float = Form(...),
    Rolling_Mean_30: float = Form(...),
    Rolling_Std_30: float = Form(...),
    Seasonality: str = Form(...)
):
    input_data = pd.DataFrame([{
        'Inventory Level': Inventory_Level,
        'Demand Forecast': Demand_Forecast,
        'Holiday/Promotion': Holiday_Promotion,
        'month': month,
        'Rolling_Mean_7': Rolling_Mean_7,
        'Rolling_Std_7': Rolling_Std_7,
        'Rolling_Mean_30': Rolling_Mean_30,
        'Rolling_Std_30': Rolling_Std_30,
        'Seasonality': Seasonality
    }])

    prediction = model.predict(input_data)[0]

    return templates.TemplateResponse("template.html", {
        "request": request,
        "result": f"Predicted Units Sold: {prediction:.2f}"
    })
