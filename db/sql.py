from sqlalchemy import create_engine
import pyodbc
from pdb import set_trace
import urllib
import pandas as pd

server = r'DESKTOP-HOKV6IO\SQLEXPRESS' 
database = 'AluraFilmes' 
username = 'myusername' 
password = 'mypassword' 
str_conn = r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=' + database + ';Trusted_Connection=yes;'

def get_odbc():
    return pyodbc.connect(str_conn)

def get_engine():
    return create_engine(f'mssql://{server}/{database}?trusted_connection=yes')

def get_df(query):
    try:
        df=pd.read_sql(con=get_engine(),sql=query)
        return df 
    except Exception as e: 
        raise Exception(f'Erro {e} - ao gerar o dataframe')

def run_query(query):
    try: 
        conn=get_odbc()
        cursor=conn.cursor()
        cursor.execute(query)
    except Exception as e: 
        raise Exception(f'Erro {e} ao executar a query.')
    finally:
        conn.close() 


