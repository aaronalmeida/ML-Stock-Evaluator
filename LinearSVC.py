######################################################################################
# Project           : Machine Learning Stock Evaluator
# Program name      : LinearSVC.py
# Author            : Aaron Almeida
# Date created      : 27/07/2019
# Purpose           : Uses Linear Support Vector Classification, a
#                     type of upervised learning where data is fit using a hyperplane 
# Revision History  : Version 1
####################################################################################


import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import statistics


style.use("ggplot")

#a list of features that would be used to fit our plane
FEATURES =  ['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ']

#function to 
def Build_Data_Set():

     #crate a pandas dataframe with all teh data
     data_df = pd.DataFrame.from_csv("key_stats_acc_perf_NO_NA.csv")
     #data_df = data_df[:100]

     #mix the data up to prevent the same stocks from being trained vs predicted on 
     data_df = data_df.reindex(np.random.permutation(data_df.index))

     
     #a numpy array without any N/A values
     X = np.array(data_df[FEATURES].values)
     X = np.nan_to_num(X)
     


     #replaces under and over performers with 0 and 1's, will be used during classifications
     y = (data_df["Status"]
          .replace("underperform",0)
          .replace("outperform",1)
          .values.tolist())

     #scale data 
     X = preprocessing.scale(X)
     Z = np.array(data_df[["stock_p_change", "sp500_p_change"]])
     Z = np.nan_to_num(Z) 
     
     return X,y,Z

     

def Analysis():

     #use a test size of 1000
     test_size = 1000
     X,y,Z= Build_Data_Set()

     #use a total investement amount of $10000
     invest_amount = 10000
     total_invests = 0

     if_market = 0
     if_strat = 0
     
     #use the linear SVC model to train the data using the outlined test size
     clf = svm.SVC(C = 1.0, kernel = "linear")
     clf.fit(X[:-test_size],y[:-test_size])

     correct_count = 0

     #predict the data using all the data
     predictions = clf.predict(X)

     #loop through all the tickers at a specific point in time to check if the prediction was correct
     for x in range(1, test_size + 1):
          if (predictions[x]==y[x]):
               correct_count += 1

          #determine the return of the market vs strategy (backtesting)
          if (predictions[x] == 1):
               invest_return = invest_amount + (invest_amount*(Z[-x][0]/100))
               market_return = invest_amount + (invest_amount*(Z[-x][1]/100))
               total_invests+=1
               if_market += market_return
               if_strat +=invest_return
               
     print("Accuracy: ",(correct_count/test_size)*100.00)
     print("Total Trades: ", total_invests)
     print("Ending with Strategy: ", if_strat)
     print("Ending with Market: ", if_market)

     #compare strategies and how much better/worse it was 
     compared = ((if_strat - if_market) / if_market)*100.0
     do_nothing = total_invests * invest_amount
     avg_market = ((if_market - do_nothing)/do_nothing)*100.0
     avg_strat = ((if_strat - do_nothing)/do_nothing)*100.0

     
     print("Compared to Market, we earned: ", str(compared) + "% more")
     print("Average investment return: ", str(avg_strat) + "% more")
     print("Average marget return: ", str(avg_market) + "% more")
     #print("Average invetsment return ")



           
Analysis()
























