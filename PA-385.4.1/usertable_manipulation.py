import mysql.connector as mydbconnection
from mysql.connector import Error

# def generate_user_table():
#     try:
#         conn = mydbconnection.connect(
#             database="RegistrationDB", user="root", password="password", port="3306"
#         )

#         cursor = conn.cursor()

#         myquery2 = "CREATE TABLE `user` (`Id` int(11) NOT NULL AUTO_INCREMENT,\
#                     `Email` varchar(100) NOT NULL,\
#                     `Name` varchar(50) NOT NULL,\
#                     `Password` varchar(30) NOT NULL,\
#                      PRIMARY KEY (`Id`))"

#         cursor.execute(myquery2)
#         print("Table is created")

#     except Error as e:
#         print("Failed tocreate table {}".format(e))

#     finally:
#         if conn.is_connected():
#             conn.close()
#             print("MySQL connection is closed")


# generate_user_table()


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



