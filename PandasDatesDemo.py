#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:39:08 2020
Author: Ankit Ghanghas

PandasDateDemo.py

This script performs basic Time Series analysis on the given oscilation data.

"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

ao=np.loadtxt('monthly.ao.index.b50.current.ascii')# load ascii file as ao numpy array

dates=pd.date_range('1950-01', periods=ao.shape[0], freq='M') #define date starting 1950-01 and monthly frequency
AO=Series(ao[:,2], index=dates)
#
AO.plot().get_figure().savefig('AtlanticOscillation.png')
plt.show()

#plt.figure()
#AO['2001':'2011'].plot()
#plt.show()
#plt.close()
nao=np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao=pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO= Series(nao[:,2], index=dates_nao)
aonao=DataFrame({'AO':AO,'NAO':NAO})

#aonao.plot(subplots=True).get_figure().savefig(')
#aonao.plot()
#plt.show()
#plt.close()

import datetime
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) & (aonao.index > datetime.datetime(1980,1,1)) & (aonao.index < datetime.datetime(1989,1,1)), 'NAO'].plot(kind='barh')
aonao.mean()
aonao.max()
aonao.min()
plt.figure()
AO_mm=AO.resample("A").median()
AO_mm.plot().get_figure().savefig('median.png')
plt.show()
#plt.close()
plt.figure()
aonao.rolling(window=12, center=False).mean().plot().get_figure().savefig('rollingmean.png')
plt.show()
