'''
This program just to test if the tables are created correctly
'''
# from multiprocessing import connection
# import sqlite3

# #connect to the database
# connection = sqlite3.connect('../data.db')
# cursor = connection.cursor()

# #get the table names [Users, Properites, ...etc...]
# all_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = [table[0] for table in all_tables]

# #output the result
# print(tables)