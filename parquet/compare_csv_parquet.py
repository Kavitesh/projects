import time
import os
import pandas as pd

# Compare file sizes
csv_size = os.path.getsize('large_data.csv') / (1024 * 1024)  # in MB
parquet_size = os.path.getsize('large_data.parquet') / (1024 * 1024)  # in MB

print(f"CSV Size: {csv_size:.2f} MB")
print(f"Parquet Size: {parquet_size:.2f} MB")


# Measure the time to read CSV
start_time = time.time()
csv_df = pd.read_csv('large_data.csv')
csv_read_time = time.time() - start_time

# Measure the time to read Parquet
start_time = time.time()
parquet_df = pd.read_parquet('large_data.parquet', engine='pyarrow')
parquet_read_time = time.time() - start_time

print(f"CSV Read Time: {csv_read_time:.4f} seconds")
print(f"Parquet Read Time: {parquet_read_time:.4f} seconds")
