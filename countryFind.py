import mariadb
import random
from geopy.distance import geodesic

DEFAULT_LOCATION = {
    "name": "Finland",
    "latitude": 61.924110,
    "longitude": 25.748151
}


#connecting database
def database_connection():
    
    config = {
            "host": "127.0.0.1",
            "port": 3306,
            "user":"root",
            "password":"12345",
            "database":"world_data"
        }
    # first try this
    try:
        # establishing connection
        conn = mariadb.connect(**config)

        # if connection successful
        print("Server Loaded!")

        # creating cursor = enables interaction with a database by executing SQL commands
        cur = conn.cursor()

        # query is the sql command
        query = "select * from countries;"

        # executing the query
        cur.execute(query)

        # getting all the data from cursor
        fetched_data = cur.fetchall()

        

    # if Error in try
    except mariadb.Error as e:
        print(f"Error in Maria DB: {e}")

    #return the fetched data to variable
    return fetched_data



# Calling the database connecting function and storing to fetched_data
fetched_data = database_connection()

# Set Default Origin Country as Finland

# Getting data randomly from the fetched data
random_country_data = random.choice(fetched_data)

# print(random_country_data)

print(f"The hint for the country in map is: {random_country_data[5]}")

user_thought_country = input("What could be the country name: ").lower()



if user_thought_country == random_country_data[1].lower():
    print("You Won")

else:
    print("You Loose:")



