import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

df = pd.read_excel('data/customer_data.xlsx')

# Prepare data for modeling
features = ['tenure_months', 'monthly_charges', 'support_tickets', 
            'days_since_last_login', 'features_used', 'payment_method']
X = df[features]
y = df['churn']

# METHOD 1: Simple Correlation
print("=== METHOD 1: CORRELATION WITH CHURN ===")
correlations = X.corrwith(y).sort_values(ascending=False)
for feature, corr in correlations.items():
    print(f"{feature:25} : {corr:.3f}")

# METHOD 2: Random Forest Feature Importance
print("\n=== METHOD 2: RANDOM FOREST IMPORTANCE ===")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

importance_df = pd.DataFrame({
    'feature': features,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

for idx, row in importance_df.iterrows():
    print(f"{row['feature']:25} : {row['importance']:.3f}")

# The 5 Risk Drivers
top_5 = importance_df.head(5)['feature'].tolist()
print(f"\n✅ THE 5 KEY BEHAVIORAL RISK DRIVERS:")
for i, driver in enumerate(top_5, 1):
    if driver == 'days_since_last_login':
        desc = "Customers who haven't logged in recently"
    elif driver == 'support_tickets':
        desc = "Customers who open many support tickets"
    elif driver == 'tenure_months':
        desc = "New customers (short tenure)"
    elif driver == 'monthly_charges':
        desc = "Customers paying high monthly fees"
    elif driver == 'features_used':
        desc = "Customers using few product features"
    else:
        desc = driver
    print(f"  {i}. {driver} → {desc}")

# Save importance for reference
importance_df.to_excel('data/feature_importance.xlsx', index=False)
print("\n✅ Saved 'data/feature_importance.xlsx'")