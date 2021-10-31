# Confidence interval for difference of two means, dependent samples

import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as st

# import data
df = pd.read_excel('ci.xlsx')
# print(df.head())

#calculate difference between weight before and after
df['Difference'] = df['Weight after (lbs)'] - df['Weight before (lbs)']
# print(df['Difference'])

#create 95% confidence interval
ci = st.norm.interval(alpha=0.95, loc = np.mean(df['Difference']), scale = st.sem(df['Difference']))
# print(ci)

low = min(ci)
high = max(ci)
print(f'From 95% Convidance intervals, we can lose weight for 12 weeks program,between {low} & {high} ibs')