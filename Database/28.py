import sqlite3
import os

from typing import List

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)

print(db_pass)