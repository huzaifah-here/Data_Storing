import mysql.connector
#git branch -m <newname>
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
#flask-sqlalchemy
def read(conn,name):
    cursor = conn.cursor()
    sql = "SELECT * FROM users"
    #sql = "SELECT * FROM users WHERE id = 2"
    cursor.execute(sql)
    result = cursor.fetchall()
    if name=='*':
        for row in result:
            print(row)
        return result
    
    # for row in result:
    #     print(row)
    res=()
    for row in result:
        if row[1] == name:
            for e in row:
                res=res+(e,)   
    print(res)
    return res 
                
# Update
def update(conn, name, email, id):
    print(id)
    print("CALL")
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

#Total ids

def total_ids(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(id) FROM users")
    total_ids = cursor.fetchone()[0]

    print(total_ids)
    return total_ids

# Use the functions
#create(conn, "John Doe", "johndoe@example.com")
read(conn,'*')
#update(conn, "Jane Doe", "janedoe@example.com", 1)
#read(conn)
#delete(conn, 1)
#read(conn)

# Close the connection
conn.close()
