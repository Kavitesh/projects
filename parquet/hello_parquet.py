import pyarrow as pa
import pyarrow.parquet as pq

# Sample data to write
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}

# Create a PyArrow Table
table = pa.table(data)

# Write the table to a Parquet file
pq.write_table(table, 'example.parquet')

# Read the Parquet file
read_table = pq.read_table('example.parquet')

# Convert the table to a Pandas DataFrame (optional)
df = read_table.to_pandas()

# Print the DataFrame
print(df)
