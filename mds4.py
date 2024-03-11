import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weight-height.csv")
#In this csv file we have to remove the outlier using mathematics
mean=df.Height.mean()
print(df.shape)
#print(mean)
std_deviation=df.Height.std()
lower_limit=mean-3*std_deviation
upper_limit=mean+3*std_deviation
#The actual valid data should between this two limits
#print(df[(df.Height>77.91)|(df.Height<54.82)]) #It is the data which doesn't lie between the valid range
#So what is valid data (data except the ouliers)
df_no_outlier=df[(df.Height<77.91)&(df.Height>54.82)] #This is valid data
print(df_no_outlier.shape) #Now The data is cleaned



#Let us use same data but different approach of data cleaning (Z-Score)
#Formual of Z-Score is Z=(x-mean)/std deviation
df['zscore']=(df.Height-df.Height.mean())/df.Height.std()  #We are adding a new column which hold the value of z_score of each row
#Finding the outlier using z-socre(-3 to 3 range is valid)
#print(df[(df.zscore<-3) |(df.zscore>3)])
df_no_outlier=df[(df.zscore<-3) &(df.zscore>3)]
print(df_no_outlier.shape)  #Error Data not  get cleaned see this problem later
