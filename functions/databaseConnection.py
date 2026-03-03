

import mariadb
import os
from dotenv import load_dotenv
from src.userName import *

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'Assects', '.env')
country_src_file_path = os.path.join(os.path.dirname(__file__), '..', 'Assects', 'demo_countries.sql')
patterns_src_file_path = os.path.join(os.path.dirname(__file__), '..', 'Assects', 'Patterns.sql')

load_dotenv(dotenv_path)

# Base configuration
config = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def database_connection_for_fetching(query, retry=False):
    conn = None
    try:
        # Try connecting with the database name
        conn = mariadb.connect(**config)
        cur = conn.cursor()
        cur.execute(query, (game_level,))
        fetched_data = cur.fetchall()
        cur.close()
        conn.close()
        return fetched_data
                
    except mariadb.Error as e:
        # If database doesn't exist, we must create it
        if "Unknown database" in str(e) and not retry:
            print(f"Database '{config['database']}' not found. Initializing...")
            setup_initial_database()
            # Try again now that database exists
            return database_connection_for_fetching(query, retry=True)
        else:
            print(f"Error in MariaDB: {e}")
            return []

def setup_initial_database():
    """Connects to MariaDB without a database to run the creation scripts."""
    # Create a copy of config without the database key
    server_config = config.copy()
    server_config.pop("database")
    
    try:
        conn = mariadb.connect(**server_config)
        cur = conn.cursor()
        
        # Execute both SQL files
        for file_path in [country_src_file_path, patterns_src_file_path]:
            with open(file_path, "r") as file:
                sql_script = file.read()
                # Split by semicolon and execute
                for statement in sql_script.split(";"):
                    if statement.strip():
                        cur.execute(statement)
            
        conn.commit()
        cur.close()
        conn.close()
    except mariadb.Error as e:
        print(f"Critical error during DB setup: {e}")