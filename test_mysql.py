import mysql.connector

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Manutddevil7",   # 🔑 your MySQL password
    database="Data"             # ✅ your new database name
)

# Test connection
if conn.is_connected():
    print("✅ Connection successful!")
else:
    print("❌ Connection failed.")

conn.close()
