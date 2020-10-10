import socket
import threading
import time
from datetime import datetime

def connection_timer():
    max_connection_interval = 60
    
    while True:
        time.sleep(1)
        current_time = time.time()  # get current time
        last_connection_interval = int(current_time - last_connection_time)  # calculate interval between last connection
        
        if last_connection_interval >= max_connection_interval and last_connection_interval % max_connection_interval == 0:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}]: Last connection was {last_connection_interval} seconds ago!")

def main():
    global last_connection_time
    hostname = socket.gethostname()
    port = 1234
    last_connection_time = time.time()

    # start server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((hostname, port))
        s.listen(1)
        
        while True:
            conn, addr = s.accept()  # accept all connections
            connection_interval = int(time.time() - last_connection_time)  # calculate interval from the last connection
            print(f"Connection from {addr[0]} | Connection interval was {connection_interval} seconds")
            conn.close()  # close connection
            last_connection_time = time.time()  # store connection time

if __name__ == "__main__":
    threading.Thread(target=connection_timer).start()
    main()
        
