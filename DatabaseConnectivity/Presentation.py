import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('Student_Details.db') #connecting sqlite database using connect()
        return conn
    except Error:
        print("Failed to create Database")

def sql_table(conn):
    cursorObj = conn.cursor()

    # Create the table in Student_Details.db

   #  cursorObj.execute("CREATE TABLE Student(std_id n(5), name char(30), subject char(35), marks decimal(3,2));")
   #
   # #  # Insert records
   #
   #  cursorObj.executescript("""
   # INSERT INTO Student VALUES(101,'James', 'Maths', 80.23);
   # INSERT INTO Student VALUES(102,'Mark', 'Science', 70.25);
   # INSERT INTO Student VALUES(103,'Alex', 'English', 90.15);
   # INSERT INTO Student VALUES(104,'John', 'Kannada', 68.35);
   # INSERT INTO Student VALUES(105,'Paul', 'Hindi', 89.45);
   # """)
   #  conn.commit()

   # #  #Read all data
    cursorObj.execute("SELECT * FROM Student")
    rows = cursorObj.fetchall()
    print("Student details:")
    for row in rows:
        print(row)

# # #Display only names
# #     cursorObj.execute("SELECT name FROM Student")
# #     rows = cursorObj.fetchall()
# #     print("Student details:")
# #     for row in rows:
# #         print(row)
# #
# #
#
# # Update query
# #
#     print("\nUpdate student marks 70.25 to 88.64 where id is 102:")
#     cursorObj.execute("UPDATE Student set marks = 88.64 WHERE std_id = 102")
#     conn.commit()
#     print("Record Updated successfully")
#     cursorObj.execute("SELECT * FROM Student")
#     rows = cursorObj.fetchall()
#     print("Student details:")
#     for row in rows:
#         print(row)

#DELETE query

    print("\nDelete the record of id 103:")
    cursorObj.execute("DELETE FROM Student WHERE std_id = 103")
    conn.commit()
    print("Record Deleted successfully")
    cursorObj.execute("SELECT * FROM Student")
    rows = cursorObj.fetchall()
    print("Student details:")
    for row in rows:
        print(row)



sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nConnection is closed.")