import seaborn as sns 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

roll = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks = [23,45,67,89,56,34,21,45,67,32,67,76,33,21,45]
sample_df = pd.DataFrame({'Roll No.' : roll, 'Marks' : marks})
#print(sample_df.head())

sns.lineplot(x='Roll No.', y = 'Marks', data = sample_df)
print(plt.title('Student Marks'))
plt.show()

seaborn_df = sns.load_dataset('titanic')
print(seaborn_df.head())

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Seaborn\hr_data.csv')
print(df.head())

sns.lineplot(x = 'number_project', y = 'average_montly_hours', data = df)
plt.figure(figsize = (12,6))
plt.title('Staffs')
plt.show()

sns.lineplot(x = 'number_project', y = 'average_montly_hours', data = df, hue = 'department')
plt.title('Staffs')
plt.show()

sns.lineplot(x = 'number_project', y = 'average_montly_hours', data = df, hue = 'left', style = 'department')
plt.title('Staffs')
plt.show()

sns.lineplot(x = 'number_project', y = 'average_montly_hours', data = df, hue = 'left', style = 'department', legend = False, palette = 'flare')  #if want to see the legend, set it to FULL
plt.title('Staffs')
plt.show()