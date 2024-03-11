import pandas as pd
import matplotlib.pyplot as pt

df=pd.read_csv("Bengaluru_House_Data.csv")
print(df.shape)
#So first we are using percentile to remove the outlier [0.001,0.999]lower and upper bound
df_no_outlier=df[(df.price>df.price.quantile(0.001)&df.price<df.price.quantile(0.999))]


