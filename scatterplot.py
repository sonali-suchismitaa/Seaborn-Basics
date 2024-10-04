import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Seaborn\hr_data.csv')
titanic_df = sns.load_dataset('titanic')
print(titanic_df.head())

'''sns.scatterplot(x='age', y='fare', data = titanic_df)
plt.title('Show')
plt.show()'''

sns.scatterplot(x='age', y='fare', data = titanic_df, hue='alive', style='class', palette='pink', alpha = 0.5)   #alpha is used for transparency
plt.title('Show')
plt.show()