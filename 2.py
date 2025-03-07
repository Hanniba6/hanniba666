import socket
import pandas as pd
import numpy as np
from datetime import datetime
import os
import zipfile

# Print your name
print("My name is hanniba")

# Get the machine name and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Machine Name: {hostname}")
print(f"IP Address: {ip_address}")

# Create customer data (10 records)
customer_data = {
    'customer_id': range(1, 11),
    'name': ['hanniba', 'alice', 'bob', 'carol', 'david', 'eve', 'frank', 'grace', 'hannah', 'john'],
    'email': ['hanniba@email.com', 'alice@email.com', 'bob@email.com', 'carol@email.com',
              'david@email.com', 'eve@email.com', 'frank@email.com', 'grace@email.com',
              'hannah@email.com', 'john@email.com']
}

# Create order data (10 records)
order_data = {
    'order_id': range(1, 11),
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'quantity': [10, 15, 5, 12, 7, 8, 20, 6, 10, 11],
    'price': [500, 400, 600, 300, 800, 450, 550, 700, 900, 100],
    'order_date': ['2024-10-01', '2024-09-30', '2024-10-10', '2024-08-20', '2024-11-15',
                   '2024-10-05', '2024-10-12', '2024-09-28', '2024-10-25', '2024-11-01']
}

# Create DataFrames
customers_df = pd.DataFrame(customer_data)
orders_df = pd.DataFrame(order_data)

# Calculate total sales (quantity * price)
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
orders_df['total_sales'] = orders_df['quantity'] * orders_df['price']

# Add status column based on the order date (New for orders after October 2024)
orders_df['status'] = np.where(orders_df['order_date'] > '2024-10-01', 'new', 'old')

# Filter records with total sales greater than 4500
high_sales_df = orders_df[orders_df['total_sales'] > 4500]

# Print Aggregated Table (Filtered Orders)
print("Aggregated Orders Table (Filtered by Total Sales > 4500):")
print(high_sales_df)

# Save the customer and order data to CSV files in the current working directory
current_directory = os.getcwd()

customers_csv_path = os.path.join(current_directory, 'customers.csv')
orders_csv_path = os.path.join(current_directory, 'orders.csv')
high_sales_csv_path = os.path.join(current_directory, 'high_sales_orders.csv')

customers_df.to_csv(customers_csv_path, index=False)
orders_df.to_csv(orders_csv_path, index=False)
high_sales_df.to_csv(high_sales_csv_path, index=False)

# Create a ZIP file with the CSV files
zip_file_path = os.path.join(current_directory, 'customer_order_files.zip')
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(customers_csv_path, os.path.basename(customers_csv_path))
    zipf.write(orders_csv_path, os.path.basename(orders_csv_path))
    zipf.write(high_sales_csv_path, os.path.basename(high_sales_csv_path))

print(f"ZIP file created at: {zip_file_path}")

