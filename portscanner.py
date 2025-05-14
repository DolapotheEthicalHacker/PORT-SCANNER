#!/bin/python3
import socket
import threading

print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is OPEN")
    except Exception as e:
        with print_lock:
            print(f"[-] Error scanning port {port}: {e}")

def port_scanner(ip, start_port, end_port, max_threads=100):
    print(f"[*] Starting scan on {ip} from port {start_port} to {end_port}")
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print("[*] Scan complete.")

if __name__ == "__main__":
    try:
        target_ip = input("Enter target IP address (e.g., 127.0.0.1): ")
        start = int(input("Enter start port (e.g., 1): "))
        end = int(input("Enter end port (e.g., 1024): "))
        port_scanner(target_ip, start, end)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
    except ValueError:
        print("[!] Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
