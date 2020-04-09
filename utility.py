import pyodbc
import psycopg2


def getconnectionlocal():
    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=localhost;'
                        'Database=master;'
                        'UID=sa;'
                        'PWD=Clam@Pay123;')
    return connection


def getconnection():
    connection = pyodbc.connect("Server=dbpaynextdev.database.windows.net;"
                        "Driver={ODBC Driver 17 for SQL Server};"
                        "Database=europa_dev;"
                        "UID=paynextdev;"
                        "PWD=Clam@Pay123;")
    return connection


def getPGConnection():
    connection = psycopg2.connect(database="netc", user="perseuspay", password="Clam@Pay123", port=5432, host="52.183.129.81")
    return connection


def getMariaConnection():
    connection = pymysql.connect(database="perseusdbv2", user="perseus", password="Clam@Pay123", port=3306, host="52.183.129.81")
    return connection