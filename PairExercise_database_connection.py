# -*- coding: utf-8 -*-
"""
Pair Programming,  Intro to Python connecting to a database

HD Sheets,  July 2024

DSE5002 pair programmming exercise, module 5

Connecting to an SQLite database from Python


     Note: This is another "stretch" example of some complicated ideas
     we haven't really talked about yet- just run through this code
     and read my comments- remember the general ideas over the next
     couple of weeks as we learn more about Python
     


SQLite is a compact SQL database,  it can handle only one user at a time
but it has full functionality

Unlike most SQL databases we don't have to provide credentials (username and
password) to it, so the connection process is easy



The process works just like it did in R

1.) create a connection from Pythoon to the database

2.) send SQL commands from Python to the database

3.) retrieve results (SQL to Python), or send changes to the database 
(Python to SQL)

4.) Process as needed in Python

5.) Clase the connection to the database at the end of the sesion


Other databases will have other types of connection libraries, you just
have to look them up (use a google command like python connect Couchbase, or
                      Python connect MySQL)

"""


#we will need some libraries, pandas and

import pandas as pd
import sqlite3 


#we will need the full file address of the chinook database file
#you need to include the full path name here
# in python, the \ has to be doubled, written as \\
#
# you can get the full path by clicking on Properties and cutting and 
# pasting

infile="C:\\Users\\sheetsh\\Documents\\Merrimack_Data_Science\\Example_data\\chinook\\chinook.db"

#create the connection to the database
#with more sophisticated databases, we would send a username
# and password
#
# the library sqlite3 is specific to SQLite, but there are libraries
# for other databases and "generic" libraries that can be used to 
# connect to virtually any database

con=sqlite3.connect(infile)

#we need a database cursor as well

cur=con.cursor()

#getting the database version

# we set up a variable to hold the SQL query we want to run
# we set this query to the database suing cur.execute
# we then fetch the output from the database,  loading it into R

sql_select_query="SELECT sqlite_version()"
cur.execute(sql_select_query)
record=cur.fetchall()
print(record)

#we can use the .tables SQL command to see the tables in the 
# database

sql_tables_query="SELECT name FROM sqlite_master WHERE (type='table');"

cur.execute(sql_tables_query)
table_listing=cur.fetchall()
print(table_listing)

# I didn't like how this printing, how is data stored in table_listing
# What type of variable is table_listing anyway?

type(table_listing)

#okay, it's a list
#
# we can do a list comprehension here, it's like a packaged for loop
# we'll see more on comprehensions later
#comprehensions are a cool feature of python, they work on iterable data types

[print(table) for table in table_listing]


#okay,let's try to load a table

sql_get_table_query="SELECT * FROM employees;"
cur.execute(sql_get_table_query)
album_list=cur.fetchall()
print(album_list)

#This returned the query as a python list
# I'd rather hava a pandas dataframe, since
# that is easier to work with
# turns out there is pandas function to do just that, using our
# connection to the database

employee_df=pd.read_sql_query(sql_get_table_query,con)

#what have we got in the data frame

employee_df.head()

#Here is a list of the columns

employee_df.columns

#since we are done, close the connection

#okay, I want to graph something, let's look at our invoices

sql_get_invoices_query="SELECT * FROM invoices;"
invoices_df=pd.read_sql_query(sql_get_invoices_query,con)

invoices_df.columns

#it looks like Total is the invoice total, let's look at a histogram
# of invoices to get an idea about what the sales patterns are

#python has no builit in graphics, load the simple
#graphics package matplotlib

import matplotlib.pyplot as plt

plt.hist(invoices_df.Total,bins=15)

# okay, that's enough for now!

# we want to close the database connection now that we are done 
# with it

con.close()

# Some last things to notice

# The SQL commands we used are mostly SQL queries
# They start with a SELECT command that states which
# variables we want, then a FROM to indicate which table
#
# Writing SQL queries is pretty important for a data scientist
# You don't have to know how to create and maintain a database, but
# running queries is pretty crucial
#
# SQL commands are traditionally capitalized SELECT, FROM,WHERE
# and names of variables and tables are mostly lowercase
#
#Resources used in creating this file

# https://pynative.com/python-sqlite/

# https://www.sqlitetutorial.net./

# https://matplotlib.org/stable/