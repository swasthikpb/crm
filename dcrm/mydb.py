# pip install my sql
# pip install my-sql connector
# pip install my-sql connector-python
import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
    )
# prepare a cursor object
cursorObject=dataBase.cursor()
# Create database
cursorObject.execute("CREATE DATABASE cdm_website")
