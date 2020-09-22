import socket
import threading
import time
from datetime import datetime

def connection_timer():
    while True:
        time.sleep(1)
        current_time = time.time()
        last_connection_interval = int(current_time - last_connection_time)

        if last_connection_interval > 4 and last_connection_interval % 5 == 0:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}]: Last connection was {last_connection_interval} seconds ago!")
        

def main():
    global last_connection_time
    hostname = socket.gethostname()
    port = 1234
    last_connection_time = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((hostname, port))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            connection_interval = int(time.time() - last_connection_time)
            print(f"Connection from {addr[0]} | Connection interval was {connection_interval} seconds")
            conn.close()
            last_connection_time = time.time()

if __name__ == "__main__":
    threading.Thread(target=connection_timer).start()
    main()
        