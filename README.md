# Customer Churn Prediction & Retention System

## Project Overview
Built a machine learning system that predicts which customers will cancel their subscription and calculates the financial impact of proactive retention.

## Structure of Github repo
```
customer-churn-prediction/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── customer_data.xlsx
│   ├── customer_data_with_risk_scores.xlsx
│   └── financial_impact.xlsx
│
├── charts/
│   └── eda_charts.png
│
├── 01_create_data.py
├── 02_eda_analysis.py
├── 03_risk_drivers.py
├── 04_risk_scoring.py
└── 05_financial_impact.py
```

## Business Impact
- **$121,200 annual revenue retained** through targeted interventions
- **26% reduction in monthly churn** (saving 202 customers per month)
- Identified **5 key behavioral risk drivers** for churn

## Key Findings
The top predictors of customer churn are:
1. **Days since last login** (30% importance) - Customers who haven't logged in for 20+ days are high risk
2. **Monthly charges** (27% importance) - Higher-paying customers are more likely to leave
3. **Tenure** (16% importance) - New customers (under 6 months) are most vulnerable
4. **Support tickets** (11% importance) - 3+ tickets indicates frustration
5. **Features used** (11% importance) - Using fewer than 4 features signals disengagement

## Technical Approach
- **Data Generation**: Created synthetic customer data (10,000 records) using Python (Pandas, NumPy)
- **Analysis**: Exploratory Data Analysis (Matplotlib, Seaborn)
- **Modeling**: Random Forest Classifier for churn prediction
- **Feature Importance**: Identified key drivers using correlation and Random Forest
- **Risk Scoring**: Built 0-100 risk scoring system for each customer

## Tools Used
- Python (Pandas, NumPy, Scikit-learn)
- Data Visualization (Matplotlib, Seaborn)
- Machine Learning (Random Forest)

## How It Works
1. System analyzes customer behavior (login frequency, support tickets, usage patterns)
2. Each customer receives a risk score (0-100)
3. High-risk customers (70+) receive targeted discounts and outreach
4. System saves 202 customers per month at 35% success rate

## Files in This Repository
|         File           |             Purpose                     |
|----------------------- |---------------------------------------- |
| 01_create_data.py      | Generates synthetic customer data       |
| 02_eda_analysis.py     | Exploratory analysis and visualizations |
| 03_risk_drivers.py     | Identifies top 5 churn predictors       |
| 04_risk_scoring.py     | Builds risk scoring system              |
| 05_financial_impact.py | Calculates ROI and revenue saved        |

## How to Run
```bash
pip install -r requirements.txt
python 01_create_data.py
python 02_eda_analysis.py
python 03_risk_drivers.py
python 04_risk_scoring.py
python 05_financial_impact.py