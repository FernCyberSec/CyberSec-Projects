import socket
import sys

TARGET = "127.0.0.1"
PORTS = [135, 139, 445, 3389, 8080]
TIMEOUT = 5
port_counter = 0

# Validate the target ONCE before scanning anything
try:
    targetip = socket.gethostbyname(TARGET)
except socket.gaierror:
    print("Something went wrong. This could be because of an invalid IP address or Port")
    sys.exit(1)


for port in PORTS:
    # Create a TCP socket for this port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    
    try:
        # connect_ex returns 0 if the port accepted the connection
        result = s.connect_ex((TARGET, port))

        if result == 0:
            port_counter += 1
            print("[+]Open port: ", port)
        else:
            print("[+]Closed port: ", port)
    finally:
         # Always hang up, even if something breaks
        s.close()

print("[*] Scan complete.", port_counter, "open port(s) found.")