import pandas as pd
import numpy as np

# Simulating a large dataset
num_rows = 10**6  # 1 million rows
data = {
    'customer_id': np.random.randint(1, 1000, num_rows),
    'transaction_amount': np.random.uniform(10, 1000, num_rows),
    'transaction_date': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2023-01-01', freq='D'), num_rows))
}

df = pd.DataFrame(data)

# Save the data as CSV
df.to_csv('large_data.csv', index=False)
df.to_parquet('large_data.parquet', engine='pyarrow')
