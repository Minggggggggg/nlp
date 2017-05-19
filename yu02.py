#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:15:14 2017

@author: chenming
"""

import pandas
obj = pandas.Series(range(3),index=['a','b','c'])
index = obj.index

import numpy as np
np.array(3)

#import matplotlib  
from numpy  import array  
import matplotlib.pyplot as plt  
fig = plt.figure()  
ax = fig.add_subplot(111)  
DataX =[1,2,3,4,5,6,7]  
DataY =[7,6,5,4,3,2,1]  
ax.scatter(DataX,DataY,15.0*array(DataX),15.0*array(DataY))  
plt.show()  
    
array(DataY)
print(array(DataY))
import numpy 
numpy.array(DataY)