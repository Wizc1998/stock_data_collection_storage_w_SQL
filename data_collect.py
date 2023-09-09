# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:38:42 2023

@author: weizi cai
"""

import yfinance


def get_open_pricec(company_name):
    return yfinance.Ticker(company_name).info['open']


#option 1: user input
#company_list = input('please enter the list of company code: ')

#option 2: pre-defined input
company_list = ['META','AMZN','GOOGL','UAL','AMC','BMW']


fetch_list = []

for company in company_list:
    try:
        print(company, get_open_pricec(company))
        fetch_list.append((company, get_open_pricec(company)))
    except KeyError:
        print('company '+company+' does not exists')

print(fetch_list)
import mysql.connector
conn = mysql.connector.connect(
   user='root', password='password', host='localhost', database='yfinancedb')

cursor = conn.cursor()

#drop table if exists
drop_table_sql = '''
    DROP TABLE IF EXISTS stock_inf;
    '''
try:
   # Executing the SQL command
   cursor.execute(drop_table_sql)
   # Commit your changes in the database
   conn.commit()
except:
   # Rolling back in case of error
   conn.rollback()

#create table statement
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS stock_inf (
        COMPANY_SYMBOL varchar(255),
        OPEN_PRICE int
    );
    '''
try:
   # Executing the SQL command
   cursor.execute(create_table_sql)
   # Commit your changes in the database
   conn.commit()
except:
   # Rolling back in case of error
   conn.rollback()

for company in fetch_list:
    #print(company)
    insert_stmt = (
       "INSERT INTO stock_inf(COMPANY_SYMBOL, OPEN_PRICE)"
       "VALUES (%s, %s)"
    )
    try:
       # Executing the SQL command
       cursor.execute(insert_stmt, company)
       
       # Commit your changes in the database
       conn.commit()

    except:
       # Rolling back in case of error
       conn.rollback()
    
    print("Data inserted for: "+company[0])


"""
Created on Sat Sep  9 14:38:42 2023

@author: weizi cai
"""











