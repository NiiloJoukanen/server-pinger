import socket
import time

def main():
    hostname = "IP HERE"  # set correct IP here
    port = 1234  # set correct port

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((hostname, port))  # connect to server
                print(f"Connected to {hostname}")  # output
                time.sleep(10)  # wait 10 seconds
            except Exception as e:  # unable to connect to server
                print(f"Error while connecting to {hostname}")
                print(e)


if __name__ == "__main__":
    main()
