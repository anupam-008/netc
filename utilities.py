import psycopg2
import pyodbc


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