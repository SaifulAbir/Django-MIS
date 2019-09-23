import socket
import time

while True:
    try:
        with socket.create_connection(('db', 3306), timeout=5):
            print("Database ready.")
            break
    except:
        print("waiting for database..")
        time.sleep(1)

