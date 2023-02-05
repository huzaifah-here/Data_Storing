import mysql.connector

#set path=%PATH%;D:\xampp\mysql\bin;
"""mysql -u username -p
    CREATE DATABASE database_name;
    SHOW DATABASES;
    USE database_name;
"""
#git
# Connect to the database
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sql_crud"
)

# Create
def create(conn, name, email):
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (name, email))
    conn.commit()
    print("Record created successfully")

# Read
def read(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Update
def update(conn, name, email, id):
    cursor = conn.cursor()
    sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
    cursor.execute(sql, (name, email, id))
    conn.commit()
    print("Record updated successfully")

# Delete
def delete(conn, id):
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Record deleted successfully")

# Use the functions
create(conn, "John Doe", "johndoe@example.com")
#read(conn)
#update(conn, "Jane Doe", "janedoe@example.com", 1)
#read(conn)
#delete(conn, 1)
#read(conn)

# Close the connection
conn.close()