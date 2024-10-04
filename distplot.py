import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Seaborn\hr_data.csv')

sns.displot((df['time_spend_company']))
print(plt.title('Plot'))
plt.show()

sns.displot((df['left']))
print(plt.title('Plot'))
plt.show()

#histograms represent the data distribution by forming bins along the range of the data and then drawing bars to show the number of observations that fall in each bin

#print(df.describe())

bins = [2,3,4,5,6,7,8,9,10]
sns.displot(df['time_spend_company'], bins = bins,  rug='True', kde = 'True', color='pink')
plt.xticks(bins)
plt.show()