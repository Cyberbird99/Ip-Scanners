import socket
import time

def scan_ports(target_ip, start_port, end_port):
    print("Starting scan on host:", target_ip)
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the connection attempt
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f'Port {port}: OPEN')

if __name__ == "__main__":
    starttime = time.time()
    
    target = input("Enter a host IP or hostname for scanning: ")
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Unable to resolve the hostname.")
        exit(1)

    start_port = 50
    end_port = 500
    
    scan_ports(target_ip, start_port, end_port)
    
    print("Duration:", time.time() - starttime)
