import psycopg2

def sql_select(query, params):
    db_connection = psycopg2.connect("dbname=golf_app")
    db_cursor = db_connection.cursor() 
    db_cursor.execute(query, params)
    results = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return results

def sql_select_no_params(query):
    db_connection = psycopg2.connect("dbname=golf_app")
    db_cursor = db_connection.cursor() 
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return results

def sql_write(query, params):
    db_connection = psycopg2.connect("dbname=golf_app")
    db_cursor = db_connection.cursor()
    db_cursor.execute(query, params)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return 

