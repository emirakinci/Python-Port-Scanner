import socket
import threading


# It avoids the output being messed up
print_lock = threading.Lock()
packet_size = 1024


# Defining a function to grab the banner after the connection is established!
def grab_banner(s, port):
    try:
        if port == 80:
            # Sending HTTP request to trigger web servers.
            s.send(b'GET / HTTP/1.1\r\n\r\n')

        # Reading now what has been received by the socket
        banner = s.recv(packet_size).decode().strip()

        return banner
    except:
        return "Unknown Service"



# Moved the scanning process inside this function
def scan_port(ip_addr, port):
    try:
        # 1. Create a socket object for each port...
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. Set Timeout 
        # Prevents the socket from hanging indefinitely if the server drops the packet (Firewall) or doesn't respond.
        sock.settimeout(1)

        # 3. Connection Attempt
        # returns 0 if successful,otherwise the error code.
        status = sock.connect_ex((ip_addr, port))

        # 4. Checking the Status...
        if status == 0:
            try:
                banner = grab_banner(sock, port)

                output = f"[+] Port {port} is OPEN! : {banner}"

            except:
                output = f"[+] Port {port} is OPEN!"

            with print_lock:
                print(output)
            
    
        # 5. Termination of the Connection
        sock.close()
    
    except:
        pass


if __name__ == "__main__":

    try:    
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
    
    except KeyboardInterrupt:
        print("\n\n[!] Scan cancelled by user. Exiting...")