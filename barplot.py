import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', data = titanic_df, hue = 'sex', palette='inferno', estimator=np.max) #hue is used to show different parameters of same class
plt.show()

sns.barplot(x='class', y='fare', data = titanic_df, hue = 'sex', palette='inferno', ci=100, errcolor='red', errwidth=10, saturation=0.3)   #ci is confidence interval, max size is 100, saturation ranges from 0-10, 0 being lightest & 10 being darkest
plt.show()