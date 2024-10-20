import mysql.connector  # Importing MySQL connector library to interact with the MySQL database
import mysql.connector.errorcode  # Importing MySQL error codes to handle specific errors

# Configuration dictionary containing the necessary details for connecting to the MySQL server
config = {
    'host': 'localhost',  # MySQL server host (usually localhost)
    'user': 'root',  # MySQL user (e.g., root)
    'password': 'somepassword'  # Password for the specified user
}

# Attempt to establish a connection to the MySQL server
try:
    # Using 'with' to ensure connection is closed properly after completion
    with mysql.connector.connect(**config) as Cnx:
        # Using another 'with' to ensure cursor is properly closed after execution
        with Cnx.cursor() as myCursor:
            try:
                # Executing SQL query to create a database called 'alx_book_store'
                # Note: There is a typo in 'CREAT', should be 'CREATE'
                myCursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;", multi=True)
                
                # If the query is successful, print a confirmation message
                print("Database 'alx_book_store' created successfully!")
                
                # Committing the transaction to apply changes to the database
                Cnx.commit()
            except mysql.connector.DatabaseError as e:
                # Catch any database-related errors (e.g., syntax error in SQL query)
                print(e)

# Catching general MySQL connector errors (such as connection issues)
except mysql.connector.Error as e:
    # Check if the error is related to access (e.g., incorrect username or password)
    if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your password or username")
    else:
        # Print any other general error
        print(e)
