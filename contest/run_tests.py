import socket
import time
import pytest
import sys

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        result = sock.connect_ex(('127.0.0.1', 30015))
        if result == 0:
            break
        else:
            print("hana not available yet, retrying...")
            time.sleep(1)
    
    pytest.main(sys.argv[1:])


if __name__ == "__main__":
    main()
