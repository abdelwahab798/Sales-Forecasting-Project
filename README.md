# 🛒 Sales Forecasting and Demand Prediction

## 📌 Project Overview  
This project builds a robust machine learning pipeline to forecast product demand using historical sales data. Accurate demand forecasting enables businesses to make data-driven decisions related to inventory, marketing strategies, and staffing.

---

## 🎯 Why This Project?  
Inaccurate demand forecasting can cause:

- **Overstocking or Understocking** → Financial losses and inefficiencies  
- **Inefficient Marketing** → Misallocation of promotional budgets  
- **Operational Disruptions** → Supply chain mismanagement  

---

## ✅ Project Outcomes  
- Improved Forecast Accuracy  
- Optimized Inventory Management  
- Enhanced Business Strategy  

---

## 🚀 Project Pipeline  
We followed a comprehensive data science workflow:

- **Data Visualization**  
  Explored relationships between features using visual tools.

- **Merging & Cleaning**  
  Merged datasets, fixed data types, handled missing values, extracted new date-based features, calculated `units_sold`, and treated outliers.

- **Exploratory Data Analysis (EDA)**  
  Analyzed relationships between features and the target variable.

- **Feature Engineering**  
  Created features like rolling mean, rolling standard deviation, etc.

- **Statistical Testing**  
  Applied ANOVA and P-values to remove irrelevant features.

- **Model Building & Evaluation**  

| Model             | MAE   | R²      | RMSE  |
|-------------------|-------|---------|-------|
| Prophet           | 8.31  | —       | —     |
| Random Forest     | 7.36  | 0.9917  | 8.66  |
| XGBoost           | 7.25  | 0.9920  | 8.49  |
| Linear Regression | 7.49  | 0.9917  | 8.69  |

- **Best Model after Tuning:**  
  - MAE: 7.20  
  - RMSE: 8.47  
  - R²: 0.9921  

- **Model Selection & Saving**  
  Selected XGBoost as the final model.

- **MLflow Integration**  
  Tracked experiments and model versions.

- **Deployment**  
  Deployed with FastAPI and an interactive HTML form allowing users to select product, store, and date for forecasts.

- **Dynamic Dashboard**  
  Created an interactive dashboard to explore feature relationships dynamically.

---

## 📂 Project Structure & Execution Order  
Run the project components in this order:

1. `project-milestone1 (1)/` – Initial planning (no code to run)  
2. `eda/` – Exploratory Data Analysis  
3. `feature_eng/` – Feature Engineering & Target Creation  
4. `dash/` – Interactive Dashboard (run `app.py`)  
5. `timeSeries/` – Prophet Model (time series forecasting)  
6. `model1/` – Random Forest Model  
7. `model2/` – XGBoost Model  
8. `model3/` – Linear Regression Model  
9. `demployment/` – FastAPI Deployment with MLflow & HTML Form (`template.html`)  

---

## 👥 Team Members & Roles

| Name                 | Role(s) & Responsibilities                                                                                                  |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Abdelwahab Amr** *(Team Leader)* | Led the team; coordinated all phases; advanced feature engineering; developed ML models; managed deployment and API integration. |
| **Hatem Tamer**       | Performed EDA, data preprocessing; contributed to ML model development and tuning.                                           |
| **Bakhom Hany**       | Designed and implemented feature engineering; created predictive variables; managed project documentation.                   |
| **Khaled Hany**       | Assisted with EDA and data visualization; supported data cleaning efforts.                                                   |
| **Mohamed Salah**     | Developed dynamic dashboard; integrated MLflow for experiment tracking; ensured smooth workflow between EDA and deployment.  |
| **Omar Abdelrahman**  | Conducted EDA; generated detailed project reports summarizing findings and model performance.                                 |

---


