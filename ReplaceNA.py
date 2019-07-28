######################################################################
# Project           : Machine Learning Stock Evaluator
# Program name      : ReplaceNA.py
# Author            : Aaron Almeida
# Date created      : 26/07/2019
# Purpose           : A script that will find the N/A data in an excel file,
#                     and replace it with the average of the data for each stock ticker
# Revision History  : Version 1
######################################################################

#import libraries
import xlrd
import xlwt
import numpy as np
from xlutils.copy import copy
from xlrd import open_workbook
import xlrd
import xlwt



#function to determine how many rows each ticker takes up and then write it in a column beside the ticker
def excelCounter()
     #open workbook & sheet 
     filename = 'key_stats.xlsx'
     workbook = xlrd.open_workbook(filename)
     sheet = workbook.sheet_by_index(0)
     sheet_name = workbook.sheet_names()[0]
     wb_out = xlwt.Workbook()
     ws_out = wb_out.add_sheet(sheet_name, cell_overwrite_ok = True)

     #initialize vars
     y = 1
     x = 3
     start = 1
     counter = 0


     #loop through ticker in each row, check whether the value of the row after is the same, if not increment count
     #if yes, then stop the counter and write how many rows the ticker used
     for i in range(0,9323):
          #find values for the current & next row
          value = sheet.cell_value(y,x)
          nextValue = sheet.cell_value(y+1,x)
          if (value == nextValue):
               y+=1
          else:
               length = y - start + 1
               print(length)
               y+=1
               #write in all the rows how many rows are occupied 
               for i in range(0,length):
                    ws_out.write(start+i,3,length)
               counter +=1
               start+=length
     wb_out.save('book2.xls')


#function to replace all the N/A's with the average of the data in the column
#the starting and ending rows are determined using the previous function
def replace()
     #open workbook & sheet
     rb = open_workbook("key_stats.xlsx")
     wk = copy(rb)
     r = wk.get_sheet(0)
     filename = 'key_stats.xlsx'
     workbook = xlrd.open_workbook(filename)
     sheet = workbook.sheet_by_index(0)
     sheet_name = workbook.sheet_names()[0]
     wb_out = xlwt.Workbook()
     ws_out = wb_out.add_sheet(sheet_name, cell_overwrite_ok = True)

     y = 1
     x = 3
     start = 1
     counter = 0
     value_list = []
     counter = 0
     index = 0
     length = 0
     nextLength = 1
     #loop through all the columns
     for m in range(0,41):
          #loop through each row to check if there is an N/A, replace it if so
          for i in range(0,9323):
               counter+=1
               if(length!=nextLength):
                    index = counter
               
               value = sheet.cell_value(i+1,m)
               length = sheet.cell_value(i+1,4)
               nextLength = sheet.cell_value(i+2,4)

               
               if(value == 'N/A'):
                    value_list = []

                    #append all the values of the column based on the index and determine its average
                    for s in range(0,int(length)):
                         value_list.append(sheet.cell_value(index+s, m))
                    value_list = value_list[0:int(length)]

                    #remove the N/A from the list for now
                    value_list = [x for x in value_list if x != 'N/A']
                    list_length = float(len(value_list))
                    if list_length == 0:
                         list_length = 1
                    avg = sum(value_list)/list_length

                    #write the new average in place of the N/A
                    r.write(i+1,m,avg)

          #reset the variables for the next column
          counter = 0
          length = 0
          nextLength = 1
          value_list = []
          index = 0
          
     wk.save('book2.xls')
               
          




excelCounter()
replace()
          




