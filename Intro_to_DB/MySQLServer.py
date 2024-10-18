import mysql.connector as mySQL
from getpass import getpass

config = {
    'host' : '172.17.176.1',
    'user' : 'enamyaovi',
    'password': getpass('Enter your password: ')
    }


try:
    with mySQL.connect(**config) as Cnx:
        with Cnx.cursor() as myCursor:
            try:
                myCursor.execute( "CREATE DATABASE alx_book_store;" , multi=True)
                print("Database 'alx_book_store' created successfully!")
                Cnx.commit()
            except mySQL.DatabaseError as e:
                print(e)
except mySQL.Error as e:
  if e.errno == mySQL.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your password")
  else:
    print(e)



