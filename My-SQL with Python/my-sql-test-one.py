import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="mytest"  # Build Database လုပ်ပြီးတဲ့အချိန်မှ ထည့်ရမယ်။
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
"""
# my_cursor.execute("CREATE TABLE teachers (name VARCHAR(255), age INTEGER(10))")
# my_cursor.execute("SHOW TABLES")
# for tb in my_cursor:
#     print(tb)
"""

# Adding students table
""""
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1 = ("Mike", 22)
# my_cursor.execute(sqlFormula, student1)   # students table တွင် data တစ်ခုတည်းပေါင်းထည့်ခြင်း

students = [
    ("Jack", 22),
    ("Mike", 24),
    ("Nick", 19),
    ("Bang", 23),
    ("Peta", 31),
]
my_cursor.executemany(sqlFormula, students)  # students table တွင် data list လုပ်ပြီး ပေါင်းထည့်ခြင်း
mydb.commit()
"""

# Data fetching form students table
"""
my_cursor.execute("SELECT * FROM students")
my_result = my_cursor.fetchall()
for i in my_result:
    print(i)
"""

#  Data fetching form students tabel by using " WHERE "
"""
# sqlFetch = "SELECT * FROM students WHERE age = 55"
# sqlFetch = "SELECT * FROM students WHERE name = 'mike'"
sqlFetch = "SELECT * FROM students WHERE name LIKE '%mi%'"  #  စာလုံး၏ ရှေ့နှင့်အလယ်တ္ငင် mi ရှိမရှိ စစ်
# sqlFetch = "SELECT * FROM students WHERE name LIKE '%ck'"  # စာလုံး၏ နောက်နှင့်အလယ်တ္ငင် mi ရှိမရှိ စစ်
# sqlFetch = "SELECT * FROM students WHERE name LIKE '%ic%'"
#
my_cursor.execute(sqlFetch)

# sqlFetch = "SELECT * FROM students WHERE name = %s"
# my_cursor.execute(sqlFetch, ("jack", ))
my_result = my_cursor.fetchall()
for i in my_result:
    print(i)
"""

# Data fetching with data limit
"""
my_cursor.execute("SELECT * FROM students LIMIT 4")
# my_cursor.execute("SELECT * FROM students LIMIT 4 OFFSET 2")
my_result = my_cursor.fetchall()
for i in my_result:
    print(i)
"""

# Data fetching by order
"""
# sqlFetch = "SELECT * FROM students ORDER BY name"
# sqlFetch = "SELECT * FROM students ORDER BY age"
# sqlFetch = "SELECT * FROM students ORDER BY name DESC"
sqlFetch = "SELECT * FROM students ORDER BY age DESC"
my_cursor.execute(sqlFetch)
my_result = my_cursor.fetchall()
for i in my_result:
    print(i)
"""

# Data Update on students table
"""
sqlUpdate = "UPDATE students SET age = 20 WHERE name = 'Nick'"
my_cursor.execute(sqlUpdate)
mydb.commit()
"""

# Delete data on students table
"""
sqlDelete = "DELETE FROM students WHERE name = 'mike'"
my_cursor.execute(sqlDelete)
mydb.commit()
"""

# add new key & vlue on students table

# my_cursor.execute("ALTER TABLE students ADD COLUMN className VARCHAR(50) NOT NULL")
my_cursor.execute("DESCRIBE students")
for i in my_cursor:
    print(i)