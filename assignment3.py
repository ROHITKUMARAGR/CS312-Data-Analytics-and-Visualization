#Rohit Kumar Agrahari
#201951129
#Section-1
#Lab Assignment 3

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from joypy import joyplot 


data_frame=pd.read_csv("grains_production_india_from_2001_to_2017.csv")
data_frame

data_frame.columns
#Below Code is to replace the columns value with NaN Value with the mean value
for x in d.columns:
    if d[x].isna().any():
        d[x]=d[x].fillna(d[x].mean())
d1=d[['Turmeric (000 tonnes)','Tobacco (000 tonnes)','Natural Rubber (000 MT)','Chillies (000 tonnes)']]
d1
#Now we will rename columns for better Visualization
#A Point plot represents an estimate of central tendency for a numeric variable by the position of scatter plot points and provides some indication of the uncertainty around that estimate using error bars
sns.pointplot(data=d1,join=False,dodge=True)
# The seaborn boxplot is a very basic plot Boxplots are used to visualize distributions. Thats very useful when you want to compare data between two groups.
sns.boxplot(data=d1)
# A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared
sns.violinplot(data=d1)
# A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.
sns.stripplot(data=d1)
sns.boxplot(data=d1)
sns.stripplot(data=d1,color="0.2")
sns.violinplot(data=d1)
sns.stripplot(data=d1,color="0.3")

#Joyplot#

joyplot(d1,overlap=0)
plt.xlabel("Production in Tonnes")

# Histogram joyplot
joyplot(d1,overlap=0,hist=True,bins=10,color = 'Red', fade = True)
plt.xlabel("Production in Tonnes")