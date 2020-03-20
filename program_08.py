#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 7 19:40:27 2020
Author: Ankit Ghanghas

program_08.py

This script takes 15 min discharge data as inputs and gives out plots of daily average  streamflow, daily average streamflow with top ten discharges marked on it and monthly average streamflow. 
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


#reads the data, parses the dates together as one reads the data starting row number 26 and reads row indexed 24 as header, uses tab as delimiter, assigns the parsed date as the index of the dataframe and stores the data for discharge in a column named discharge.
df=pd.read_table("WabashRiver_DailyDischarge_20150317-20160324.txt",parse_dates=True, header=24,skiprows=1, delimiter= '\t', usecols=[2,4], index_col= ['date'], names = ['date','discharge'])

#Plotting the daily mean discharge
daily_mn=df.resample("D").mean() #resamples data by averaging over the data for a day to get mean daily discharge.
daily_mn.plot(style='r-') #plots the daily mean discharge with specified style ( a red dashed line)
plt.xlabel("Date") # specifies the xlabel as "Date"
plt.ylabel("Discharge(in cfs)") #specifies the y label as Discharge(in cfs)
plt.title("Daily Average Streamflow") # specifies the title of the plot
plt.savefig("daily_average_stream.pdf") # saves the plot as a pdf
plt.close() # closes the plot

#Plots the top 10 discharges on the Daily mean discharge plot.
ten_max=daily_mn.nlargest(10,'discharge')#makes a dataframe of top ten discharges in daily mean data
daily_mn.plot(style='r-') #plots the daily mean discharge
plt.scatter(ten_max.index,ten_max.discharge,color='g',label='Top 10 maximum daily flows') # scatter plots the top ten discharges and specifies the label for them
plt.legend(['Discharge','Top 10 maximum flows']) # creates a legend for the plot
plt.xlabel("Date")
plt.ylabel("Discharge(in cfs)")
plt.title("Top 10 Maximum Daily Discharge")
plt.savefig("top_ten_max.pdf")
plt.close()

#Plotting the monthly average streamflow
monthly=df.resample("M").mean() #resamples the original discharge data by averaging over the data for a month to 
monthly.plot()# plots the data in monthly dataframe. since we only have one data column (discharge) other than the indices so it will plot the data column with the indices.
plt.xlabel("Date")
plt.ylabel("Discharge(in cfs)")
plt.title("Monthly Average Streamflow")
plt.savefig("monthly_average_stream.pdf")
plt.close()


