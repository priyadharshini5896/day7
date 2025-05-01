import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the existing database
conn = sqlite3.connect("sales_data.db")

# SQL query to summarize sales
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Load data into a DataFrame
df = pd.read_sql_query(query, conn)

# Print the summary
print("Sales Summary:")
print(df)

# Create bar chart for revenue
df.plot(kind='bar', x='product', y='revenue', legend=False, title='Revenue by Product')
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Optional: Save chart as an image
# plt.savefig("sales_chart.png")

# Close connection
conn.close()
