# stock_data_collection_storage_w_SQL
 this is a tiny python program with using yfinance to pull fresh stock data, and populate local MySQL tables

# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:08:11 2023

@author: jason(weizi)
"""

#readme 

this is the readme file for data_collect.py

in the code there are two options for getting my company list

option 1 is user input while option 2 is developer pre defined company list

firstly, I ued yfinance component to get the information I need for each companies in the 
list including:

company open price of that day

then, I stored the information alone with company stock code into a tuple

I used the mysql package to iteratively put the tuples into a newly created sql table 
with name: stock_inf

in terms of validation, when I pulled the data with yfinance, I will check whether if the
company exists, if its a fake company code, I will catch that error.