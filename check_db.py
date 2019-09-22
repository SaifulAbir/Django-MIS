import socket
import time

while True:
    try:
        with socket.create_connection(('db', 3306), timeout=5):
            break
    except:
        print("waiting for db")
        time.sleep(1)

