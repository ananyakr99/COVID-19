#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/anuma/Desktop/Ananya/MyResearch/COVID19')

#Importing Data 
data=pd.read_csv('dataset.csv')
total_cases=data['Cases']
index=data['Index']

#Plotting the exponential curve
fig = plt.figure()
rect=[0.1, 0.15, 0.8, 0.8]
ax=fig.add_axes(rect, frameon=True)
plt.scatter(index,total_cases,color='red',s=10,label='Cumulative number of COVID-19 positive cases')
plt.xlabel('Date')
plt.ylabel('Number of total cases')
plt.title('Trend of COVID-19 in India')
ax.set_xticklabels(['30-Jan-20','01-Mar-20','05-Mar-20','15-Mar-20','25-Mar-20','08-Apr-20','16-Apr-20','24-Apr-20','05-May-20'])
plt.legend()
plt.show()

#Logarithmic Values - Straight Line
log_y=[]
for i in total_cases:
    log_y.append(np.log(i))
fig = plt.figure()
rect=[0.15, 0.1, 0.8, 0.8]
ax=fig.add_axes(rect, frameon=True)
plt.scatter(index,log_y,color='blue',s=10)
plt.xlabel('Date')
plt.ylabel('Logarithmic Values')
plt.title('Trend of COVID-19 with logarithmic values')
ax.set_xticklabels(['30-Jan-20','15-Feb-20','05-Mar-20','15-Mar-20','25-Mar-20','08-Apr-20','16-Apr-20','24-Apr-20','05-May-20'])
plt.legend()
plt.show()

#Pre-Lockdown Data
before_lockdown=total_cases[0:26]
index_bl=index[0:26]
fig = plt.figure()
rect=[0.15, 0.1, 0.8, 0.8]
ax=fig.add_axes(rect, frameon=True)
plt.scatter(index_bl,before_lockdown,color='red',s=10,label='Cumulative number of COVID-19 positive cases')
plt.xlabel('Date')
plt.ylabel('Number of total cases')
plt.title('Trend of COVID-19 in India before the Lockdown')
ax.set_xticklabels(['k','30-Jan-20','05-Feb-20','15-Feb-20','25-Feb-20','05-Mar-20','15-Mar-20','23-Mar-20'])
plt.legend()
plt.show()

#Pre-Lockdown Logarithmic Graph
log_y2=[]
for i in before_lockdown:
    log_y2.append(np.log(i))
fig = plt.figure()
rect=[0.15, 0.1, 0.8, 0.8]
ax=fig.add_axes(rect, frameon=True)
plt.scatter(index_bl,log_y2,color='blue',label='Logarithmic values',s=10)
ax.set_xticklabels(['k','30-Jan-20','05-Feb-20','15-Feb-20','25-Feb-20','05-Mar-20','15-Mar-20','23-Mar-20'])
plt.xlabel('Date')
plt.ylabel('Logarithmic Values')
plt.title('Trend of COVID-19 in India before the Lockdown')
plt.legend()
plt.show()

#Best Fit Line
from statistics import mean
import matplotlib.pyplot as plt
xs=index_bl
ys=log_y2

#Finding Slope,Intercept
m=(((mean(xs)*mean(ys)) - mean(xs*ys))/((mean(xs)*mean(xs)) - mean(xs*xs)))
b=mean(ys) - m*mean(xs)
print(m,b)

#Linear Regression
fig = plt.figure()
rect=[0.15, 0.1, 0.8, 0.8]
ax=fig.add_axes(rect, frameon=True)
regression=[(m*i)+b for i in xs]
plt.scatter(xs,ys,color='blue',s=15)
ax.set_xticklabels(['k','30-Jan-20','05-Feb-20','15-Feb-20','25-Feb-20','05-Mar-20','15-Mar-20','23-Mar-20'])
plt.plot(xs,regression,color='red',label='Best Fit Line')
plt.xlabel('Date')
plt.ylabel('Number of active cases before the Lockdown in Logarithmic Scale')
plt.title('Plotting the Best Fit Line')
plt.legend()
plt.show()

#Future Prediction
x2=index[25:]
prediction=[(m*i)+b for i in x2]
fig = plt.figure()
rect=[0.15, 0.1, 0.8, 0.8]
ax=fig.add_axes(rect, frameon=True)
plt.scatter(index,log_y,color='blue',s=10,label='Total Cases when Lockdown was enforced')
plt.plot(xs,regression,color='red',label='Best Fit Line for Cases before Lockdown was enforced')
plt.plot(x2,prediction,color='green',label='Extension of the Best Fit Line')
ax.set_xticklabels(['30-Jan-20','15-Feb-20','05-Mar-20','15-Mar-20','25-Mar-20','08-Apr-20','16-Apr-20','24-Apr-20','05-Apr-20'])
plt.xlabel('Date')
plt.ylabel('Total number of cases')
plt.title('Prediction of the potential number of cases without the Lockdown by extending the Best-Fit Line')
plt.legend()
plt.show()
