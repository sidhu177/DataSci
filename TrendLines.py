# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:24:07 2018

Taken from Beginning Python Visualization by Shai Vaingast, Apress Publishing

@author: SIDHARTH
"""

from pylab import *
import csv
from time import gmtime, mktime

filepath = 'C:\\Users\\SIDHARTH\\Python\\DataSci\\Charts.csv'

data = []
for row in csv.reader(open(filepath),delimiter='\t'):
    data.append(row)
    
header = data[0]
values = array(data[2:])
yearday = zeros(len(values[:,0]))
for i, day in enumerate(values[:,0]):
    market_close_time = (int(day[6:]),int(day[:2]),int(day[3:5]),16,0,0,0,0,0)
    yearday[i] = gmtime(mktime(market_close_time)).tm_yday
    
for i in range(1,5):
    plot(yearday,values[:,1],label=header[i],linewidth=3)
    
text(yearday[0],values[0,1],values[0,0],ha='center')
text(yearday[-1],values[-1,1],values[-1,0],ha='center')

grid()
legend(loc='best')
xlabel('Days from start of the year '+values[0,0][6:])
ylabel('Stock price [USD]')
title('NASDAQ-100 (IXNDX) Stock price, period %s-%s' (values[-1,0],values[0,0]))
savefig('C:Users/SIDHARTH/Python/DataSci/stock_price.png', dpi=150)