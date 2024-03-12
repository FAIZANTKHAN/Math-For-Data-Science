import pandas as pd
import matplotlib.pyplot as pt
df=pd.read_csv("revenue.csv")

#df.plot(x='company',y='revenue',kind='bar')
#pt.show()  #In this case we cant able to compare the revenues of company so we have to se log axis
df.plot(x='company',y='revenue',kind='bar', log=True)
pt.show() #Now You can clearly identify and compare the revenues