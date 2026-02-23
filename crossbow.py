import mariadb
import random
import os
from dotenv import load_dotenv

load_dotenv()

def database_connection():
 
    config = {
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT", 3306)), # Cast to int; 3306 is the fallback
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")

 }

    try:
        conn = mariadb.connect(**config)
        print("Server Loaded!\n")

        cur = conn.cursor()

        query = "SELECT * FROM Patterns ;"
        cur.execute(query)

        fetched_data = cur.fetchall()

        return fetched_data

    except mariadb.Error as e:
        print(f"Error in MariaDB: {e}")
        return []

fetched_pattern = database_connection()
print(fetched_pattern)