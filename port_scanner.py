import socket
import time

# Target Information
target_ip = input("Please insert an IP address!:\n")
target_ports = [21, 22, 80, 443, 3389] # most widely used ports...


for port in target_ports:
    # 1. Create a socket object for each port...
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Set Timeout 
    # Prevents the socket from hanging indefinitely if the server drops the packet (Firewall) or doesn't respond.
    sock.settimeout(2)

    # 3. Connection Attempt
    # returns 0 if successful,otherwise the error code.
    status = sock.connect_ex((target_ip, port))

    # 4. Checking the Status...
    if status == 0:
        print(f"[+] Connection to {target_ip}:{port} has been successfully established!\n")
    else:
        print(f"[-] Cannot establish connection to {target_ip}:{port}!\n")

    # 5. Termination of the Connection
    sock.close()
    print("The socket is closed and the resources are freed!\n")

    # 6. Waiting 0.5 seconds before trying to connect to the next port!
    time.sleep(0.5) 
    print("***************************************\n")
    
    if(port != target_ports[-1]):
        print("Starting to connect to the next port...\n")