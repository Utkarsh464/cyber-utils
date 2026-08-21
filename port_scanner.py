"""TCP connect port scanner — scan a target IP or hostname across a port range."""

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = 50


def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        return port
    return None


def main():
    parser = argparse.ArgumentParser(description="TCP connect port scanner")
    parser.add_argument("target", help="target IP or hostname")
    parser.add_argument("--start", type=int, default=1, help="start port")
    parser.add_argument("--end", type=int, default=1024, help="end port")
    args = parser.parse_args()

    print("simple port scanner")
    print("-------------------")
    print(f"\nscanning {args.target} from port {args.start} to {args.end}...\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for port in executor.map(
            lambda p: scan_port(args.target, p), range(args.start, args.end + 1)
        ):
            if port is not None:
                print(f"port {port} is open")
                open_ports.append(port)

    if open_ports:
        print(f"\nopen ports: {open_ports}")
    else:
        print("\nno open ports found")


if __name__ == "__main__":
    main()
