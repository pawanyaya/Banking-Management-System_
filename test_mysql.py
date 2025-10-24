import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="**********",   
    database="Your DataBaseName"             
)


if conn.is_connected():
    print(" Connection successful!")
else:
    print(" Connection failed.")

conn.close()
