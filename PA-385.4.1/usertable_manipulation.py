# Importing MySQL connector and error handling classes
import mysql.connector as mydbconnection
from mysql.connector import Error


# Creates the 'user' table inside the RegistrationDB database
def generate_user_table():
    try:
        conn = mydbconnection.connect(
            database="RegistrationDB", user="root", password="password", port="3306"
        )
        
        # Get a cursor
        cursor = conn.cursor()

        # Creating a 'User' table
        myquery2 = "CREATE TABLE `user` (`Id` int(11) NOT NULL AUTO_INCREMENT,\
                    `Email` varchar(100) NOT NULL,\
                    `Name` varchar(50) NOT NULL,\
                    `Password` varchar(30) NOT NULL,\
                     PRIMARY KEY (`Id`))"
        
        # Execute a query
        cursor.execute(myquery2)
        print("Table is created")

    except Error as e:
        print("Failed tocreate table {}".format(e))

    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")


generate_user_table()


# Inserts the multiple data into 'user' table 
def insert_into_table(email, name, password):
    try:
        conn = mydbconnection.connect(database='RegistrationDB', user='root',password='password', port ='3306')
        
        cursor = conn.cursor()
        mySql_insert_query = """INSERT INTO user (email, name, password) VALUES (%s, %s, %s) """                  

        record = (email, name, password)
        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print("Record inserted successfully into User table \n")

    except Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


insert_into_table('ywbaek@perscholas.org', 'young', 'letsgomets')
insert_into_table('mcordon@perscholas.org', 'marcial', 'perscholas')
insert_into_table('mhaseeb@perscholas.org', 'haseeb', 'platform')


# Retrieves and prints all user records from the 'user' table
def get_all_users():
    try:
        conn = mydbconnection.connect(database='RegistrationDB', user='root', password='password', port ='3306')
        cursor = conn.cursor()

        sql_select_query = "select * from user"
        cursor.execute(sql_select_query)

        # fetch result
        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0])
            print("Email = ", row[1])
            print("Name = ", row[2])
            print("Password  = ", row[3], "\n")


    except Error as error:
        print("Failed to fetch data from user table {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

get_all_users()


# Retrieves user details based on the provided name
def get_user_by_name(name):
    
    conn = mydbconnection.connect(database='RegistrationDB', user='root', password='password', port ='3306')
    cursor = conn.cursor()

    sql_select_query = """select * from user where name = %s"""


    # set variable in query
    cursor.execute(sql_select_query, (name,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        print("Email = ", row[1])
        print("Password  = ", row[3], "\n")
        
        cursor.close()
        conn.close()
        print("MySQL connection is closed")

get_user_by_name('young')
get_user_by_name('marcial')
get_user_by_name('haseeb')


# Validates login by checking if a user exists with the given email and password
def validate_user(email, password):
    try:
        conn = mydbconnection.connect(database='RegistrationDB', user='root', password='password', port ='3306')
        cursor = conn.cursor()

        sql_select_query = """SELECT * FROM user WHERE Email = %s AND Password = %s"""
      
        cursor.execute(sql_select_query, (email, password))
        record = cursor.fetchall()
        # print(record)

        # Return True if at least one matching user exists
        if len(record) > 0:
            return True
        else:
            return False
        

    except Error as e:
        print("Error while validating user:", e)
        return False

    finally:
        if conn.is_connected():
            conn.close()

print(validate_user('mcordon@perscholas.org','perscholas'))
print(validate_user('shiv@perscholas.org','perscholasss'))


# Updates a user's name and password based on their email
def update_user(name, password, email):
    
    try:
        conn = mydbconnection.connect(database='RegistrationDB', user='root', password='password', port ='3306')
        cursor = conn.cursor()

        sql_update_query = """UPDATE user SET name = %s, password = %s where email = %s"""
      
        cursor.execute(sql_update_query, (name, password, email))
        conn.commit() 
       
        # Check if any row was updated
        return cursor.rowcount > 0
        

    except Error as e:
        print("Error while validating user:", e)
        return False

    finally:
        if conn.is_connected():
            conn.close()

print(update_user('shivani', 'perscholas','mcordon@perscholas.org'))
