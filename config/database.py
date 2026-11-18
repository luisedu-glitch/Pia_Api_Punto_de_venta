import mysql.connector as mc

DB_CFG = {
    "host": "localhost",
    "user": "root",
    "password": "Unafacil123",
    "database": "pia_intefaz",
}


def get_conn():
    return mc.connect(**DB_CFG)
