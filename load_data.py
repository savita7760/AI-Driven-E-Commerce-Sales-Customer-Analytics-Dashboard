import pandas as pd
import sqlite3

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Connect SQLite database
conn = sqlite3.connect("database.db")

# Store CSV data into SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded successfully!")

# Close connection
conn.close()