import mysql.connector

"""
This is a simple python script file 
Used to create a database on mysql using
mysql connector in python (mysqlx for windows).
The connections will be wrapped in a try and except block
the try block will contain the connector, cursor and queries
since this is a simple script there will be no need for nested try blocks
if the query 'database creation' is successful and throws no errors
then the else block with a single print statement should execute
the finally block closes the connection to our server
the except block will contain a tuple of mysql.connector general Exceptions base Exception errors
"""

try: # contains connector, cursor and queries for database creation
    server_connection = mysql.connector.connect(
                                host = 'localhost',
                                user = 'root',
                                password = 'somepassword'
                                                    ) # Most of the kwargs provided here are generic.

    mycursor = server_connection.cursor()# creates a cursor for executing the query for database creation

    """
    After this block of comment is the query/execute statement section. This could have been included in a nested try block
    But for the sake of simplicity we would keep everything in one block
    The down side is that if there are any exceptions raised we will have a hard time knowing which line of code raised the error
    But for a simple code as this it will be straight forward.
    """
    mycursor.execute(
                    """
                    CREATE DATABASE IF NOT EXISTS alx_book_store;
                    """
                    ) #the if not exists clause exists 'pun intended' to prevent a database error from being raised
    

except mysql.connector.Error as e: # since our script file is a simple script we will stick to the base exception error for DBs in mysql
    print('Something went wrong: {}'.format(e))

except BaseException as e: # Base exception for other type of errors
    print(f'Error: {e}')
else:
    print("Database: 'alx_book_store' created successfully!") #if no error/exception arises we want to print this
finally:
    mycursor.close()
    server_connection.close() #releasing all resources
