#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 7 19:40:27 2020
Author: Ankit Ghanghas
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

df=pd.read_table("WabashRiver_DailyDischarge_20150317-20160324.txt",parse_dates=True, header=24,skiprows=1, delimiter= '\t', usecols=[2,4], index_col= ['date'], names = ['date','discharge'])


daily_mn=df.resample("D").mean()
daily_mn.plot(style='r-')
plt.xlabel("Date")
plt.ylabel("Discharge(in cfs)")
plt.title("Daily Average Streamflow")
plt.savefig("daily_average_stream.pdf")
plt.close()

ten_max=daily_mn.nlargest(10,'discharge')
daily_mn.plot(style='r-')
plt.scatter(ten_max.index,ten_max.discharge,color='g',label='Top 10 maximum daily flows')
plt.legend(['Discharge','Top 10 maximum flows'])
plt.xlabel("Date")
plt.ylabel("Discharge(in cfs)")
plt.title("Top 10 Maximum Daily Discharge")
plt.savefig("top_ten_max.pdf")
plt.close()

monthly=df.resample("M").mean()
monthly.plot()
plt.xlabel("Date")
plt.ylabel("Discharge(in cfs)")
plt.title("Monthly Average Streamflow")
plt.savefig("monthly_average_stream.pdf")
plt.close()


