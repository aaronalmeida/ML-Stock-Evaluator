######################################################################
# Project           : Machine Learning Stock Evaluator
# Program name      : QuandlRequest.py
# Author            : Aaron Almeida
# Date created      : 27/07/2019
# Purpose           : a program to retreive daily closing prices of ticker
#                     using quandls API
# Revision History  : Version 1
######################################################################
import pandas as pd
import os
import quandl
import time

auth_tok = open('authtoken.txt','r').read()

##data = quandl.get("WIKI/KO",trim_start = '2000-12-12"', trim_end = '2018-12-30')
##
##print(data["Adj. Close"])

path = ('C:/Users/Aaron/Downloads/intraQuarter')

def Stock_Prices():
     df = pd.DataFrame()
     statspath = path + "/_KeyStats"
     stock_list = [x[0] for x in os.walk(statspath)]

     #get the tickers by reading through the directory
     for each_dir in stock_list[1:]:
          try:

               #write api calls to get closing data of each stock in the s&p 500
               ticker = each_dir.split("\\")[1]
               print(ticker)
               name = "WIKI/"+ticker.upper()
               data = quandl.get(name,
                                 trim_start = '2000-12-12"',
                                 trim_end = '2018-12-30',
                                 authtoken = auth_tok)
               data[ticker.upper()] = data['Adj. Close']
               df = pd.concat([df, data[ticker.upper()]],axis = 1)

         #try again after 10 seconds, just in case server had a slip      
          except Exception as e:
               print(str(e))
               time.sleep(10)
               try:
                    ticker = each_dir.split("\\")[1]
                    print(ticker)
                    name = "WIKI/"+ticker.upper()
                    data = quandl.get(name,
                                      trim_start = '2000-12-12"',
                                      trim_end = '2018-12-30',
                                      authtoken = auth_tok)
                    data[ticker.upper()] = data['Adj. Close']
                    df = pd.concat([df, data[ticker.upper()]],axis = 1)

               except Exception as e:
                    print(str(e))
     df.to_csv("stock_prices.csv")
          
Stock_Prices()
