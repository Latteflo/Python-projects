import socket

target = input("Enter the IP address: ")
port_range = [int(x) for x in input("Enter the port range (start, end): ").split(",")]
  
def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # Returns 0 if port is open
        if result == 0:
            print(f"Port {port} is open")
        else:
            print('Port', port, 'is not open') 
        s.close()
        
if __name__ == "__main__":
    start_port, end_port = port_range
    scan_ports(target, start_port, end_port)
