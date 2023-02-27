import sqlite3 as sql # import the sqlite3 module ​

# Create a connection object that represent the database you want to create and/or use  in order to ​
# use the SQLite module imported in line 1 this ​ensures that we can perform various database operations. 

# connect() = connection method to creates db and connects to it if it does not exist
# otherwise it will just connect to and use the exsisting DB
conn = sql.connect("FilmFlixAppProject /1_SQLiteDB/filmflix.db")

# Now create a cursor object after establishing a connection in step 2 "conn = sql.connect()", 

# cursor() = cursor object
cursor = conn.cursor()