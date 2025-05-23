🛒 Sales Forecasting and Demand Prediction
📌 Project Overview
This project aims to build a robust machine learning pipeline to forecast product demand based on historical sales data. Accurate demand forecasting helps businesses make data-driven decisions in inventory management, marketing strategies, and staffing.

🎯 Why This Project?
Inaccurate demand forecasting can lead to:

Overstocking or Understocking → Causing financial losses and inefficiencies

Inefficient Marketing → Misallocation of promotional budgets

Operational Disruptions → Misjudging demand can harm the supply chain

✅ Project Outcomes
Improved Forecast Accuracy

Optimized Inventory Management

Enhanced Business Strategy

🚀 Project Pipeline
We followed a complete data science workflow:

Data Visualization

Explored relationships between columns using visual analysis.

Merging & Cleaning

Merged datasets, fixed data types, and handled missing values.

Extracted new features from date columns and calculated units_sold.

Detected and treated outliers.

EDA (Exploratory Data Analysis)

Analyzed relationships between features and the target.

Feature Engineering

Created features like rolling mean, rolling std, etc.

Statistical Testing

Used ANOVA and P-Values to identify and drop irrelevant features.

Model Building
Trained 4 models:

Prophet

MAE: 8.31

Random Forest

MAE: 7.36 | R²: 0.9917 | RMSE: 8.66

XGBoost

MAE: 7.25 | R²: 0.9920 | RMSE: 8.49

✅ Best Model after Tuning

Tuned MAE: 7.20, RMSE: 8.47, R²: 0.9921

Linear Regression

MAE: 7.49 | R²: 0.9917 | RMSE: 8.69

Model Selection & Saving

Selected XGBoost as the final model and saved it.

MLflow Integration

Tracked all experiments using MLflow.

Deployment with FastAPI + HTML Form

Deployed the model using FastAPI and built a cool interactive HTML form that allows users to select product, store, and date to generate a forecast easily.

Dynamic Dashboard

Built an interactive dashboard for exploring feature relationships.

📂 Project Structure & Execution Order
To run the full project, follow this order:

project-milestone1 (1)/ → Initial project planning (no code to run)

eda/ → Exploratory Data Analysis

feature_eng/ → Feature engineering & target creation

dash/ → Interactive dashboard (run app.py)

timeSeries/ → Prophet model (time series forecasting)

model1/ → Random Forest

model2/ → XGBoost

model3/ → Linear Regression

demployment/ → FastAPI deployment with MLflow and HTML form (form.html)

| Name                               | Role(s) & Responsibilities                                                                                                                                                                                              |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Abdelwahab Amr** *(Team Leader)* | Led the team, coordinated all project phases, performed advanced feature engineering, developed machine learning models, managed model deployment using FastAPI, and integrated the API with the interactive front-end. |
| **Hatem Tamer**                    | Conducted exploratory data analysis (EDA), handled data preprocessing, contributed to model development and tuning, and supported validation of machine learning models.                                                |
| **Bakhom Hany**                    | Designed and implemented feature engineering techniques, created new predictive variables, managed project documentation, and ensured clear communication of technical details.                                         |
| **Khaled Hany**                    | Assisted with exploratory data analysis, generated insightful visualizations to uncover data patterns, and supported data cleaning efforts.                                                                             |
| **Mohamed Salah**                  | Developed the dynamic dashboard for interactive data visualization, integrated MLflow to track and manage experiments, and ensured smooth workflow between data exploration and deployment.                             |
| **Omar Abdelrahman**               | Performed exploratory data analysis (EDA) and generated detailed project reports, summarizing findings and model performance to facilitate informed decision-making.                                                    |


