import pandas as pd
import numpy as np

# Set random seed so results are repeatable
np.random.seed(42)

# Number of customers
n_customers = 10000

# Create customer IDs
customer_id = range(1, n_customers + 1)

# 1. Tenure (how many months they've been customer: 1 to 36 months)
tenure = np.random.randint(1, 37, n_customers)

# 2. Monthly charges ($20 to $150)
monthly_charges = np.random.uniform(20, 150, n_customers).round(2)

# 3. Total support tickets (0 to 10)
support_tickets = np.random.poisson(lam=2, size=n_customers)
support_tickets = np.clip(support_tickets, 0, 10)

# 4. Days since last login (0 to 60)
days_since_last_login = np.random.exponential(scale=10, size=n_customers).astype(int)
days_since_last_login = np.clip(days_since_last_login, 0, 60)

# 5. Number of features used (out of 10 possible features)
features_used = np.random.randint(1, 11, n_customers)

# 6. Payment method (0 = credit card, 1 = PayPal, 2 = bank transfer)
payment_method = np.random.choice([0, 1, 2], n_customers, p=[0.5, 0.3, 0.2])

# 7. Churn calculation based on behavior
churn_probability = (
    (monthly_charges / 150) * 0.2 +
    (support_tickets / 10) * 0.3 +
    (days_since_last_login / 60) * 0.4 +
    (1 - features_used/10) * 0.1
)

churn_probability = churn_probability + np.random.uniform(-0.2, 0.2, n_customers)
churn_probability = np.clip(churn_probability, 0, 1)
churn = (churn_probability > 0.5).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'customer_id': customer_id,
    'tenure_months': tenure,
    'monthly_charges': monthly_charges,
    'support_tickets': support_tickets,
    'days_since_last_login': days_since_last_login,
    'features_used': features_used,
    'payment_method': payment_method,
    'churn': churn
})

# Save to data folder
df.to_excel('data/customer_data.xlsx', index=False)

print("✅ Data created! Check 'data/customer_data.xlsx'")
print(f"Total customers: {n_customers}")
print(f"Customers who churned: {df['churn'].sum()} ({df['churn'].mean()*100:.1f}%)")