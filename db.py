import psycopg2
import psycopg2.extras as e

def db_connection():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "Kales3",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "Users")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
