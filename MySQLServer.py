# import mysql.connector  # Importing MySQL connector library to interact with the MySQL database
# import mysql.connector.errorcode  # Importing MySQL error codes to handle specific errors

# # Configuration dictionary containing the necessary details for connecting to the MySQL server
# config = {
#     'host': 'localhost',  # MySQL server host (usually localhost)
#     'user': 'root',  # MySQL user (e.g., root)
#     'password': 'somepassword'  # Password for the specified user
# }

# # Attempt to establish a connection to the MySQL server
# try:
#     # Using 'with' to ensure connection is closed properly after completion
#     with mysql.connector.connect(**config) as Cnx:
#         # Using another 'with' to ensure cursor is properly closed after execution
#         with Cnx.cursor() as myCursor:
#             try:
#                 # Executing SQL query to create a database called 'alx_book_store'
#                 # Note: There is a typo in 'CREAT', should be 'CREATE'
#                 myCursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;", multi=True)
                
#                 # If the query is successful, print a confirmation message
#                 print("Database 'alx_book_store' created successfully!")
                
#                 # Committing the transaction to apply changes to the database
#                 Cnx.commit()
#             except mysql.connector.DatabaseError as e:
#                 # Catch any database-related errors (e.g., syntax error in SQL query)
#                 print(e)

# # Catching general MySQL connector errors (such as connection issues)
# except mysql.connector.Error as e:
#     # Check if the error is related to access (e.g., incorrect username or password)
#     if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your password or username")
#     else:
#         # Print any other general error
#         print(e)

import mysql.connector

"""
A simple Python script to create a MySQL database using mysql-connector.
The connection, cursor, and query execution are handled in a try-except block.
If the database is created successfully, a success message is printed.
"""

# Initialize variables to None to prevent NameError if connection fails
server_connection = None
mycursor = None

try:
    # Establish a connection to the MySQL server
    server_connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='somepassword'
                            )
    mycursor = server_connection.cursor()  # Create a cursor for executing the query

    # Execute the SQL query to create the database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")

except mysql.connector.Error as e:
    print(f'Something went wrong with MySQL: {e}')

except BaseException as e:
    print(f'An error occurred: {e}')

else:
    print("Database 'alx_book_store' created successfully!")  # This block executes if no exceptions occur

finally:
    # Ensure resources are released, but only if they were successfully created
    if mycursor:
        mycursor.close()
    if server_connection and server_connection.is_connected():
        server_connection.close()
    else:
        print('Exiting...')
