import mysql.connector

def koneksiDatabase():
    try:
        mydb = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = "",
            database = "customer_service"
        )
        cursor = mydb.cursor() 
        return mydb, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None