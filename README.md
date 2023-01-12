# Data-Insights
A collection of data analysis and visualization projects for insights generation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read in customer data
customer_data = pd.read_csv("path/to/customer_data.csv")

# Perform necessary data cleaning
customer_data = customer_data.dropna()

# Explore the data using pandas methods
print(customer_data.head())
print(customer_data.describe())

# Create visualizations
plt.hist(customer_data["age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Perform K-Means clustering
X = customer_data[["age", "income", "purchase_amount"]]
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Add cluster labels to the data
customer_data["cluster"] = y_kmeans

# Generate insights
print(customer_data.groupby("cluster").mean())
