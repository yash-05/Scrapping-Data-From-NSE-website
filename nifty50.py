#!/usr/bin/env python
# coding: utf-8

# In[15]:


import urllib
from bs4 import BeautifulSoup
import requests
from datetime import date
import datetime

diff = date.today() - datetime.timedelta(days=364)

fromDate = diff.strftime('%d-%m-%Y')
toDate = (date.today()).strftime('%d-%m-%Y')
url = 'https://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=NIFTY%2050&fromDate='+ str(fromDate)+'&toDate='+ str(toDate)
#print(url)


#url = 'https://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=NIFTY%2050&fromDate=15-02-2018&toDate=14-02-2019'
req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0'})
source = urllib.request.urlopen(req).read()
simple_soup = BeautifulSoup(source)
csv = simple_soup.find(id='csvContentDiv').text
#print(csv)

vsc = csv.replace(':', ',') #to replace the colon from comma so that we can split the string with only commas in next step
#print(vsc)

data = vsc.split(',')
#print(data)




def TURNOVER(data):
    turnover = []
    for i in range(len(data)):
        if i > 12 and (i - 13)%7 == 0:
            turnover.append(float(data[i].replace("\"", "")))
            
    return turnover


def SHARES_TRADED(data):
    shares = []
    for i in range(len(data)):
        if i > 11 and (i - 12)%7 == 0:
            shares.append(float(data[i].replace("\"", "")))

    return shares


def CLOSE(data):
    close = []
    for i in range(len(data)):
        if i > 10 and (i - 11)%7 == 0:
            close.append(float(data[i].replace("\"", "")))
            
    return close

def LOW(data):
    low = []
    for i in range(len(data)):
        if i > 9 and (i - 10)%7 == 0:
            low.append(float(data[i].replace("\"", "")))
            
    return low


def HIGH(data):
    high = []
    for i in range(len(data)):
        if i > 8 and (i - 9)%7 == 0:
            high.append(float(data[i].replace("\"", "")))
            
    return high


def OPEN(data):
    Open = []
    for i in range(len(data)):
        if i > 7 and (i - 8)%7 == 0:
            Open.append(float(data[i].replace("\"", "")))
            
    return Open


def COMPUTE_MEAN(data):
    turnover_mean = sum(TURNOVER(data)[-10:])/10
    shares_traded_mean = sum(SHARES_TRADED(data)[-10:])/10
    close_mean = sum(CLOSE(data)[-10:])/10
    low_mean = sum(LOW(data)[-10:])/10
    high_mean = sum(HIGH(data)[-10:])/10
    open_mean = sum(OPEN(data)[-10:])/10
    
    return turnover_mean,shares_traded_mean,close_mean,low_mean,high_mean,open_mean
    
(turnover_mean,shares_traded_mean,close_mean,low_mean,high_mean,open_mean) = COMPUTE_MEAN(data)

print("The Rolling Mean of Turnover of last 10 days is " + str(turnover_mean)+"\u20B9" + " Cr")

#I only print the mean of turnover ,however the mean of shares traded, close,low, high and open can also be computed fro the computed mean function.

