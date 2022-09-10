import sqlite3
import os

from typing import List

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
# print(db_pass)

def execute_query(connection, 
                  query_sql: str) -> List:
    '''
    Функція для виповнення запроса
    :param з'єднання з бд, sql-запрос
    :return: результат виповнення запроса
    '''
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result

def unwrapp_query_result(records: List) -> None:
    '''
    Функція для красивого вивода результату в консоль
    :param список строк
    '''
    for record in records:
        print(*record)

def get_invoice_items() -> None:
    '''
    d
    '''
    query_sql = f'''
            SELECT sum(UnitPrice * Quantity)
                FROM invoice_items;
    '''
    result = execute_query(connection, query_sql)
    unwrapp_query_result(result)

get_invoice_items()
