import mariadb
import os
from dotenv import load_dotenv
from src.userName import *

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'Assects', '.env')


load_dotenv(dotenv_path)


def database_connection_for_fetching(query):
 
    config = {
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT", 3306)), # Cast to int; 3306 is the fallback
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")

 }

    try:
        conn = mariadb.connect(**config)
        print("Game Loaded!\n")

        cur = conn.cursor()

        cur.execute(query, (game_level,))

        fetched_data = cur.fetchall()

        return fetched_data

    except mariadb.Error as e:
        print(f"Error in MariaDB: {e}")
        return []
