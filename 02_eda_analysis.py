import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create charts folder if it doesn't exist
os.makedirs('charts', exist_ok=True)

# Load the data
df = pd.read_excel('data/customer_data.xlsx')

# 1. Basic info
print("=== DATA OVERVIEW ===")
print(df.head())
print("\n=== DATA TYPES ===")
print(df.dtypes)
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 2. Compare churned vs stayed
print("\n=== CHURNED VS STAYED (AVERAGES) ===")
churn_summary = df.groupby('churn').mean()
print(churn_summary)

# 3. Visualize differences
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Tenure comparison
df[df['churn']==0]['tenure_months'].hist(ax=axes[0,0], alpha=0.7, label='Stayed', bins=20, color='green')
df[df['churn']==1]['tenure_months'].hist(ax=axes[0,0], alpha=0.7, label='Churned', bins=20, color='red')
axes[0,0].set_title('Tenure: Stayed vs Churned')
axes[0,0].legend()

# Days since last login
df[df['churn']==0]['days_since_last_login'].hist(ax=axes[0,1], alpha=0.7, label='Stayed', bins=20, color='green')
df[df['churn']==1]['days_since_last_login'].hist(ax=axes[0,1], alpha=0.7, label='Churned', bins=20, color='red')
axes[0,1].set_title('Days Since Login: Stayed vs Churned')
axes[0,1].legend()

# Support tickets
df[df['churn']==0]['support_tickets'].hist(ax=axes[1,0], alpha=0.7, label='Stayed', bins=10, color='green')
df[df['churn']==1]['support_tickets'].hist(ax=axes[1,0], alpha=0.7, label='Churned', bins=10, color='red')
axes[1,0].set_title('Support Tickets: Stayed vs Churned')
axes[1,0].legend()

# Monthly charges
df[df['churn']==0]['monthly_charges'].hist(ax=axes[1,1], alpha=0.7, label='Stayed', bins=20, color='green')
df[df['churn']==1]['monthly_charges'].hist(ax=axes[1,1], alpha=0.7, label='Churned', bins=20, color='red')
axes[1,1].set_title('Monthly Charges: Stayed vs Churned')
axes[1,1].legend()

plt.tight_layout()
plt.savefig('charts/eda_charts.png', dpi=150)
plt.show()

print("\n✅ Charts saved to 'charts/eda_charts.png'")