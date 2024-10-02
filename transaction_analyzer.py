import pandas as pd
import random
import matplotlib.pyplot as plt

# Step 1: Generate Random Transaction Data
products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Cash']

def generate_random_transactions(num_transactions=100):
    data = []
    for _ in range(num_transactions):
        product = random.choice(products)
        price = random.uniform(50, 1000)
        location = random.choice(locations)
        payment_method = random.choice(payment_methods)
        data.append([product, price, location, payment_method])
    return pd.DataFrame(data, columns=['Product', 'Price', 'Location', 'Payment Method'])

# Step 2: Analyze Data
df = generate_random_transactions(100)

# Most Sold Products
most_sold_products = df['Product'].value_counts()

# Revenue by Region
revenue_by_region = df.groupby('Location')['Price'].sum()

# Payment Method Distribution
payment_method_distribution = df['Payment Method'].value_counts()

# Step 3: Plot the Results
def plot_data():
    plt.figure(figsize=(15, 5))

    # Plot 1: Most Sold Products
    plt.subplot(1, 3, 1)
    most_sold_products.plot(kind='bar', color='skyblue')
    plt.title('Most Sold Products')
    plt.xlabel('Product')
    plt.ylabel('Count')

    # Plot 2: Revenue by Region
    plt.subplot(1, 3, 2)
    revenue_by_region.plot(kind='bar', color='lightgreen')
    plt.title('Revenue by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Revenue')

    # Plot 3: Payment Method Distribution
    plt.subplot(1, 3, 3)
    payment_method_distribution.plot(kind='bar', color='coral')
    plt.title('Payment Method Distribution')
    plt.xlabel('Payment Method')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()

# Run the analysis and plot the results
plot_data()
