import pandas as pd
import numpy as np

df=pd.read_csv("AB_NYC_2019.csv")
#print(df.price.quantile(0.25))
#print(df.price.quantile(0.75))
percentile_99=df.price.quantile(0.99)
df_withno_outlier=df[df.price<=percentile_99]
#print(df_withno_outlier.sample(5))  #I just take out values that are above 0.99 percentile
#print(df_withno_outlier.describe())

#According to my analysis by my method the minimum value remain in the data set that is why no. of values is more(99 percentile part)
#But in the below case which is soln the teacher remove both the extreme part the minimum(1 percentile) as well as the highest(99 percentile)

#or
min_thresold, max_thresold = df.price.quantile([0.01,0.999]) #But in this case the data which are lie between the 1 and 99 percentile is shown
df2 = df[(df.price>min_thresold)&(df.price<max_thresold)]
#print(df2.sample(5))
#print(df2.describe())


