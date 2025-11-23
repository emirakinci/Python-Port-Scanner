import socket
import threading


# It avoids the output being messed up
print_lock = threading.Lock()


# Moving the scanning process inside this function
def scan_port(ip_addr, port):
    try:
        # 1. Create a socket object for each port...
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. Set Timeout 
        # Prevents the socket from hanging indefinitely if the server drops the packet (Firewall) or doesn't respond.
        sock.settimeout(2)

        # 3. Connection Attempt
        # returns 0 if successful,otherwise the error code.
        status = sock.connect_ex((ip_addr, port))

        # 4. Checking the Status...
        if status == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN!")
    
        # 5. Termination of the Connection
        sock.close()
    
    except:
        pass



# Target Information
target_ip = input("Please insert an IP address!:\n")

# Storing the generated threads for possible use in future
generated_threads = list()

print(f"\nScanning {target_ip} started... (Please wait)\n")
print("*" * 50)



for port in range(1, 1025):    
    # Generating threads for each port number
    t = threading.Thread(target=scan_port, args=(target_ip, port))
    generated_threads.append(t) # inserting in a list the generated threads

    t.start() # executing the scan for that specific port given to each thread


# Wait for all threads to finish
for thread in generated_threads:
    thread.join()

print("*" * 50)
print("Scanning completed.")