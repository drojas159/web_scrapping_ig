import psycopg2
from psycopg2 import Error

def connection():
    try:
        
        hostname = 'localhost'
        username = 'postgres'
        password = 'root'
        database = 'mental_data_ig'
        port = 5433

        connection = psycopg2.connect(user=username,
                                    password=password,
                                    host=hostname,
                                    port=port,
                                    database=database)


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    

    return connection

