from multiprocessing import connection
import sqlite3


  
connection = sqlite3.connect('../../data.db')
cursor = connection.cursor()

#get the table names [Users, Properites, ...etc...]
all_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [table[0] for table in all_tables]


insert_queries = [
  
  "INSERT INTO {table} VALUES(?)"
  
]

def gen_data_into_tables():
  for table in tables:
    if table == 'Users' or table == 'Properties' or table == "Transactions":
      
      query = "INSERT INTO {table_name} VALUES(?)".format(table_name=table)
      
      for i in range(10):
        cursor.execute(query, (table[:-1].lower() + str(i), ))
        
      

gen_data_into_tables()
      
      

# query = "INSERT INTO {table} VALUES(?)".format(table="Users")

# all_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# print(list(all_tables))
# cursor.execute(query, ("user_1", ))
# cursor.execute(query, ("user_2", ))
# cursor.execute(query, ("user_3", ))
# cursor.execute(query, ("user_4", ))

see_all_user = "SELECT * FROM Properties"
see_single = "SELECT * FROM Users WHERE Users.user_id = (?)"
result = cursor.execute(see_all_user)
print(list(result))

result2 = cursor.execute(see_single, ("user_3", ))
print(list(result2))
