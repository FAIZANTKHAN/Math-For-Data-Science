import pandas as pd
import numpy as np
df=pd.read_csv("salary.csv")
print(df.income.quantile(0.75))  #quantile is used to calculate the percentile
print(df.income.quantile(0.25))
print(df.income.quantile(1))
percentile_99=df.income.quantile(0.99)
print(df[df.income>percentile_99])  #We have to delete this Outlier (Unwanted value )
df_no_outlier=df[df.income<=percentile_99]  #we create a new data frame from df which doen't contain percentile_99
print(df_no_outlier)


