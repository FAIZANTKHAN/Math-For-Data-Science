import pandas as pd
import numpy as np
df=pd.read_csv("movie_revenues.csv")
df['revenue_mln']=df['revenue'].apply(lambda x:x/100000) #New column is added which will contain the revenue in million
_,mean,std,*_=df.revenue_mln.describe() #mean and std are variable that store the value of  mean and std deviation
def get_z_score(value,mean,std):
    return (value-mean)/std  #This function calculate the value of  z_score

df['z_score']=df.revenue_mln.apply(lambda x:get_z_score(x,mean,std))  #It will create a new column of z_socre which will store all the value of z_score column wise
print(df[df.z_score>3])  #It will show the outlier according to the z_score but we not able to find all the outlier so we aare going to use modified z_score

#First we calculate MAD
def get_mad(s):
    median=np.median(s)
    diff=abs(s-median)
    np.median(diff)
    return MAD

MAD=get_mad(df.revenue_mln)
median=np.median(df.revenue_mln)


#Showing Error
