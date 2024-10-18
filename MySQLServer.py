import mysql.connector
from getpass import getpass

import mysql.connector.errorcode

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password': getpass('Enter your password: ')
    }


try:
    with mysql.connector.connect(**config) as Cnx:
        with Cnx.cursor() as myCursor:
            try:
                myCursor.execute( "CREATE DATABASE IF NOT EXISTS alx_book_store;" , multi=True)
                print("Database 'alx_book_store' created successfully!")
                Cnx.commit()
            except mysql.connector.DatabaseError as e:
                print(e)
except mysql.connector.Error as e:
  if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your password")
  else:
    print(e)



