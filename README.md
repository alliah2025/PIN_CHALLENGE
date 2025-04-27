Interactive Programming CTF Challenge Solution (IT6)

Overview
This project is a brute-force script created to solve a local Capture the Flag (CTF) challenge hosted on `http://127.0.0.1:8888`. The goal was to discover the correct 3-digit PIN code by submitting HTTP POST requests to the `/verify` endpoint and interpreting the server's response.

Tools & Technologies Used
- Python – To write and execute the brute-force automation script.
- HTTP (Hypertext Transfer Protocol) – To communicate with the local web server via raw POST requests.
- Wireshark – For analyzing HTTP traffic and understanding request/response behavior.
 Process
-Server Application (provided)

Solution Process
1. Understanding the Challenge
   - The web form accepts a PIN and shows an error message (`Incorrect number`) if the guess is wrong.
   - I assumed that the correct response would not include that error string, and I could use this behavior to detect the correct PIN.

2. Approach
   - I wrote a Python script that sends a POST request for each 3-digit combination (`000` to `999`) using raw sockets.
   - The response is checked for the "Incorrect number" phrase. If it's missing, that means the PIN is correct.

3. Building the Request
   - I crafted the HTTP POST request manually to include the `magicNumber` parameter in the body.
   - I used `socket` to directly connect and communicate with the server for full control of the request.

4. Handling the Response
   - I received the response in chunks using `recv(1024)` inside a loop until the server closed the connection.
   - The full response was decoded and checked for the error message.

5. Finding the Correct PIN
   - The loop breaks as soon as a successful response is detected.
   - A delay (`time.sleep(1.2)`) was added between requests to respect server-side rate limiting or cooldowns.

How to Run This Project
•	Open and run the server application
•	Type this   localhost:8888  in web browser
•	Run the python pin_point.py script
Make sure the server is active before running the script. The script will loop through 3-digit PINs and stop when the correct one is found.

VIDEO PRESENTATION LINK IN GDRIVE 
https://drive.google.com/drive/folders/12CCciAZoOA2D-KBo_o2tfZK0yP67aHMd?usp=sharing

