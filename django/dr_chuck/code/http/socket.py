# This Python code is a very low-level HTTP client built using sockets. 
# It manually connects to a web server, sends an HTTP request, 
# and prints the server’s response.

# The socket module lets Python communicate over networks (TCP/IP).
import socket 

# AF_INET → Use IPv4
# SOCK_STREAM → Use TCP (reliable connection)
# This creates a TCP socket, like opening a phone line.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connects to:
# - Host: data.pr4e.org
# - Port: 80 (standard HTTP port)
# Now your program is connected to the web server.
mysock.connect(('data.pr4e.org', 80)) 

# This is a raw HTTP request:
# - GET → Request a web page
# - HTTP/1.0 → HTTP version
# - \r\n\r\n → Marks end of HTTP headers
# - .encode() → Converts string to bytes (sockets send bytes)
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Sends the HTTP request to the server.
mysock.send(cmd) 

# Receives up to 512 bytes at a time from the server.
# Servers send responses in chunks.
while True: 
    data = mysock.recv(512) 
    
    # When server finishes sending data, recv() returns empty bytes.
    # That means end of response. 
    if len(data) < 1: 
        break 

    # decode() → Converts bytes to string
    # end='' → Prevents extra new lines
    # Prints:
    # - HTTP headers
    # - HTML content of the page
    print(data.decode(),end='') 

# Closes the network connection properly.
mysock.close()