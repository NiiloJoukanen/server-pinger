import socket
import time

def main():
    hostname = "DESKTOP-AS9GGMQ"
    port = 1234

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((hostname, port))
                print(f"Connected to {hostname}")
                time.sleep(3)
            except Exception as e:
                print(f"Error while connecting to {hostname}")
                print(e)


if __name__ == "__main__":
    main()