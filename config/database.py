import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_CFG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_conn():
    return mysql.connector.connect(**DB_CFG)