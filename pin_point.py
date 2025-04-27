import socket
import time

HOST = "127.0.0.1"
PORT = 8888
DELAY = 1.2 

def try_pin(pin):
    pin_str = f"{pin:03d}"  
    data = f"magicNumber={pin_str}"

    request = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{data}"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(request.encode())