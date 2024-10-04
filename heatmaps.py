import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the flights dataset from Seaborn
'''flight_df = sns.load_dataset('flights')
print(flight_df.head())

# Pivot the DataFrame to get 'month' as the index, 'year' as columns, and 'passengers' as values
flight_df_pivot = flight_df.pivot(index="month", columns="year", values="passengers")
print(flight_df_pivot.head())

# Now create the heatmap with the pivoted data
plt.figure(figsize=(12, 6))
ax = sns.heatmap(flight_df_pivot, annot=True, fmt='d', linecolor='k', linewidths=5, cmap = 'Blues')
plt.title("Monthly Passengers per Year")
#plt.show()

grid_kws = {'height_ratios':(.4, 0.05), 'hspace':0.4}
f, (ax, cbar_ax) = plt.subplots(2,1, gridspec_kw=grid_kws, figsize=(12,8))
sns.heatmap(flight_df_pivot, annot=True, fmt='d', cbar_kws={"orientation": "horizontal"}, ax=ax, cmap='Blues')
sns.heatmap(flight_df_pivot, cbar_kws={"orientation": "horizontal"}, ax=cbar_ax, cmap='Blues', cbar=True,cbar_ax=cbar_ax)
plt.show()'''

titanic_df = sns.load_dataset('titanic')
numeric_cols = titanic_df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = titanic_df[numeric_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix for Titanic Dataset')
plt.show()
