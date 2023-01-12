import pandas as pd
import matplotlib.pyplot as plt

# Read in happiness data
happiness_data = pd.read_csv("path/to/happiness_data_2022.csv")

# Explore the data using pandas methods
print(happiness_data.head())
print(happiness_data.describe())

# Create visualizations
happiness_data.plot(kind='bar', x='Country', y='Happiness_Score')
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.show()

# Perform statistical analysis
correlation = happiness_data['Happiness_Score'].corr(happiness_data['GDP_Per_Capita'])
print(correlation)

# Generate insights
highest_happiness = happiness_data.loc[happiness_data['Happiness_Score'].idxmax()]
print("Country with highest happiness score in 2022: ", highest_happiness['Country'])
