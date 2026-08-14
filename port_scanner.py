"""TCP connect port scanner — scan a target IP or hostname across a port range."""

import socket
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = 50

print("simple port scanner")
print("-------------------")

target = input("enter target ip or hostname: ")
start_port = int(input("start port: "))
end_port = int(input("end port: "))

print(f"\nscanning {target} from port {start_port} to {end_port}...\n")

open_ports = []


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        return port
    return None


with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    for port in executor.map(scan_port, range(start_port, end_port + 1)):
        if port is not None:
            print(f"port {port} is open")
            open_ports.append(port)

if open_ports:
    print(f"\nopen ports: {open_ports}")
else:
    print("\nno open ports found")
