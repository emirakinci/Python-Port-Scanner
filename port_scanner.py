import socket

# Target Information
target_ip = "216.58.204.238" # Google IP (obtained via pinging in my terminal)
target_port = 80 ## http

# 1. Create Socket Object
# AF_INET: IPv4 Address Family
# SOCK_STREAM: TCP Protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Set Timeout
# Prevents the socket from hanging indefinitely if the server drops the packet (Firewall) or doesn't respond.
sock.settimeout(2) 

# 3. Connection Attempt
# returns 0 if successful,otherwise the error code.
status = sock.connect_ex((target_ip, target_port))

# 4. Checking the Status...
if status == 0:
    print(f"[+] Connection to {target_ip}:{target_port} has been successfully established!")
else:
    print(f"[-] Cannot establish connection to {target_ip}:{target_port}")

# 5. Termination of the Connection
sock.close()
print("The socket is closed and the resources are freed!")