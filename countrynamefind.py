import mariadb
import os
from dotenv import load_dotenv
import random
from userName import *

load_dotenv()

def database_connection():
    config = {
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT", 3306)), # cast to int; 3306 is the fallback
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os. getenv("DB_NAME")
    }
    try:
        conn = mariadb.connect(**config)
        print("Server Loaded!\n")
        
        cur = conn.cursor()

        query = "SELECT name FROM countries;"
        cur.execute(query)

        fetched_data = cur.fetchall()

        return fetched_data

    except mariadb.Error as e:
        print(f"Error in MariaDB: {e}")
        return[]



fetched_countries = database_connection()


# Pick random target country
random_country_name = random.choice(fetched_countries)[0]

random_country_length = len(random_country_name)

print(random_country_length, random_country_name)

print("Guess the country: ")
for i in range(random_country_length):
    print(" _ ", end="")
