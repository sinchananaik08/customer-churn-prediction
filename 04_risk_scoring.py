import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

df = pd.read_excel('data/customer_data.xlsx')

# Features
features = ['tenure_months', 'monthly_charges', 'support_tickets', 
            'days_since_last_login', 'features_used', 'payment_method']
X = df[features]
y = df['churn']

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

# Get churn probability (0 to 1)
churn_probability = rf.predict_proba(X)[:, 1]

# Convert to risk score (0 to 100)
df['risk_score'] = (churn_probability * 100).round(1)

# Add risk category
def categorize_risk(score):
    if score < 30:
        return 'Low Risk'
    elif score < 60:
        return 'Medium Risk'
    elif score < 80:
        return 'High Risk'
    else:
        return 'Critical Risk'

df['risk_category'] = df['risk_score'].apply(categorize_risk)

# Show results
print("=== RISK SCORE DISTRIBUTION ===")
print(df['risk_category'].value_counts())

print("\n=== SAMPLE HIGH-RISK CUSTOMERS (Risk Score >= 70) ===")
high_risk = df[df['risk_score'] >= 70].head(10)
print(high_risk[['customer_id', 'risk_score', 'days_since_last_login', 
                  'support_tickets', 'tenure_months', 'churn']])

# Save with risk scores
df.to_excel('data/customer_data_with_risk_scores.xlsx', index=False)
print("\n✅ Saved 'data/customer_data_with_risk_scores.xlsx'")

print("\n=== RECOMMENDED INTERVENTIONS ===")
print("Critical Risk (80-100): Send 30% discount + personal email")
print("High Risk (70-79): Send 20% discount + feature tutorial")
print("Medium Risk (30-69): Send engagement email (no discount)")
print("Low Risk (0-29): No action needed")