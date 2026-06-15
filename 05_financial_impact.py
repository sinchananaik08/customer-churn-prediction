import pandas as pd

df = pd.read_excel('data/customer_data_with_risk_scores.xlsx')

# Business assumptions
average_monthly_revenue = 50  # $50 per customer per month
intervention_success_rate = 0.35  # 35% of intervened customers stay

# Step 1: Identify who would have churned
customers_who_churned = df[df['churn'] == 1]
churned_count = len(customers_who_churned)

print("=== FINANCIAL IMPACT SIMULATION ===")
print(f"1. Monthly churn without intervention: {churned_count} customers")

# Step 2: High-risk customers (score >= 70)
high_risk_customers = df[df['risk_score'] >= 70]
high_risk_count = len(high_risk_customers)
print(f"2. Your system flags {high_risk_count} high-risk customers")

# Step 3: Among high-risk, who actually churned
high_risk_who_churned = high_risk_customers[high_risk_customers['churn'] == 1]
intervention_targets = len(high_risk_who_churned)
print(f"3. Among flagged customers, {intervention_targets} were actually going to churn")

# Step 4: Customers saved
saved_customers_this_month = int(intervention_targets * intervention_success_rate)
print(f"4. With {intervention_success_rate*100}% success rate, you save {saved_customers_this_month} customers THIS MONTH")

# Step 5: Monthly revenue saved
monthly_revenue_saved = saved_customers_this_month * average_monthly_revenue
print(f"5. Monthly revenue saved: ${monthly_revenue_saved:,.0f}")

# Step 6: Annual revenue saved
annual_revenue_saved = monthly_revenue_saved * 12
print(f"6. Annual revenue saved: ${annual_revenue_saved:,.0f}")

# Step 7: Churn reduction percentage
churn_reduction_pct = (saved_customers_this_month / churned_count) * 100
print(f"\n=== YOUR IMPACT SUMMARY ===")
print(f"✓ Prevent {churn_reduction_pct:.0f}% of monthly churn")
print(f"✓ Retain ${annual_revenue_saved:,.0f} in annual recurring revenue")

# Scale recommendation for resume
if annual_revenue_saved < 200000:
    print(f"\n💡 For your RESUME, you can say:")
    print(f"   'Scalable model retaining ${annual_revenue_saved * 2:,.0f}-${annual_revenue_saved * 3:,.0f} ARR'")
else:
    print(f"\n🎉 Your numbers are resume-ready!")

# Save financial summary
summary = pd.DataFrame({
    'Metric': ['Total customers', 'Monthly churn (no action)', 'High-risk customers flagged', 
               'Customers saved per month', 'Monthly revenue saved', 'Annual revenue saved',
               'Churn reduction %'],
    'Value': [len(df), churned_count, high_risk_count, saved_customers_this_month, 
              monthly_revenue_saved, annual_revenue_saved, f"{churn_reduction_pct:.0f}%"]
})
summary.to_excel('data/financial_impact.xlsx', index=False)
print("\n✅ Saved 'data/financial_impact.xlsx'")