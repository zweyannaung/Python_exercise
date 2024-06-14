import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="mytest" # Build Database လုပ်ပြီးတဲ့အချိန်မှ ထည့်ရမယ်။
)

my_cursor = mydb.cursor()

# Building Database
"""
# my_cursor.execute("CREATE DATABASE mytest")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
"""

# Building Table

# my_cursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
my_cursor.execute("SHOW TABLES")
for tb in my_cursor:
    print(tb)