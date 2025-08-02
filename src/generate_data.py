import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Define the number of samples
n_samples = 1000

# 1. Generate `customer_id`
customer_ids = [f'C{i:04d}' for i in range(1, n_samples + 1)]

# 2. Generate `subscription_type` with realistic proportions
subscription_types = np.random.choice(
    ['Basic', 'Premium', 'Enterprise'],
    size=n_samples,
    p=[0.6, 0.3, 0.1]  # 60% Basic, 30% Premium, 10% Enterprise
)

# 3. Generate `monthly_bill` based on subscription type
monthly_bill = np.zeros(n_samples)
monthly_bill[subscription_types == 'Basic'] = np.random.normal(50, 5, sum(subscription_types == 'Basic'))
monthly_bill[subscription_types == 'Premium'] = np.random.normal(150, 15, sum(subscription_types == 'Premium'))
monthly_bill[subscription_types == 'Enterprise'] = np.random.normal(500, 50, sum(subscription_types == 'Enterprise'))

# 4. Generate other numerical features
data_usage_gb = np.random.gamma(shape=2, scale=15, size=n_samples) + monthly_bill / 10 # Correlated with bill
support_tickets_opened = np.random.poisson(lam=1.5, size=n_samples)
last_login_days_ago = np.random.exponential(scale=20, size=n_samples)
contract_length_months = np.random.choice([1, 12, 24], size=n_samples, p=[0.5, 0.3, 0.2])
customer_service_score = np.random.normal(4.0, 0.8, n_samples).clip(1, 5) # Score is between 1 and 5

# 5. Introduce churn based on a logical formula to make it a solvable problem
# Churn is more likely for customers with low service scores, many support tickets, or on short contracts
churn_probability = (
    0.2 * (6 - customer_service_score) / 5 +
    0.1 * support_tickets_opened / 5 +
    0.1 * (12 - contract_length_months) / 12
)
churn_probability = np.clip(churn_probability, 0.05, 0.5) # Ensure a reasonable range
churn = (np.random.rand(n_samples) < churn_probability).astype(int)

# 6. Introduce missing values in a key column
n_missing = int(n_samples * 0.05) # 5% missing values
missing_indices = np.random.choice(n_samples, n_missing, replace=False)
data_usage_gb[missing_indices] = np.nan

# Create the final DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    'subscription_type': subscription_types,
    'monthly_bill': monthly_bill.round(2),
    'data_usage_gb': data_usage_gb.round(2),
    'support_tickets_opened': support_tickets_opened,
    'last_login_days_ago': last_login_days_ago.round(2),
    'contract_length_months': contract_length_months,
    'customer_service_score': customer_service_score.round(2),
    'churn': churn
})

# Save the dataset to a CSV file
df.to_csv('data/dataset-big.csv', index=False)

# Display the first few rows and a brief summary to confirm it worked
print("First 5 rows of the generated DataFrame:")
print(df.head())
print("\nDataFrame Info:")
df.info()