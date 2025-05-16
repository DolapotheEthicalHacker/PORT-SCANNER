# PORT-SCANNER
#  Python Port Scanner

*Python Port Scanner* is a simple yet powerful terminal-based tool developed by *Dolapotheethicalhacker*. It performs multithreaded TCP port scanning to identify open ports on a target IP address or hostname. Designed with ethical hacking and cybersecurity learners in mind, this script helps you quickly assess a host's network exposure and is a useful utility for penetration testing, network diagnostics, and vulnerability scanning.

---

##  What It Does

This scanner attempts to connect to a range of TCP ports on a user-specified target (such as an IP or domain name). By attempting to establish socket connections, the tool determines which ports are open and actively accepting connections. It is built using Python's socket module for low-level network communication and concurrent.futures for concurrent execution. The multithreading mechanism dramatically speeds up scans compared to traditional sequential approaches, making it practical for quickly identifying open ports up to 1024 or even across all 65535 ports.

---

##  Features

-  *Multithreaded Scanning* — utilizes Python's ThreadPoolExecutor for high-speed scanning across multiple ports simultaneously.
-  *Accurate Open Port Detection* — checks if ports are accepting TCP connections and outputs only open ports.
-  *Lightweight and Beginner-Friendly* — no external dependencies, easy to understand and customize.
-  *Terminal-Based Interface* — scan targets directly from your terminal or command line.
-  *Fully Offline Tool* — does not require internet connection unless scanning an external domain.
-  *Ethical Hacking Utility* — excellent for educational purposes, internal audits, and CTF practice environments.

---

##  File Overview

- port_scanner.py  
  → The main Python script that:
  - Accepts user input for the target IP or hostname.
  - Attempts socket connections to a specified range of ports.
  - Runs threads to speed up scanning.
  - Outputs open ports in real-time with simple formatting.

---

##  How It Work

1. The user inputs a target (like 127.0.0.1 or scanme.nmap.org).
2. The script defines a range of TCP ports to scan (default: 1–1024).
3. Using socket.socket, it attempts to connect to each port.
4. With ThreadPoolExecutor, multiple threads perform scans in parallel.
5. If a connection to a port is successful, the port is marked as "open".
6. Open ports are printed out to the terminal.

This mimics the behavior of common tools like Nmap (though without service detection or advanced options), and is ideal for quick scans or embedding in larger Python-based security projects.

---

##  Requirements

No external libraries are required — this project uses only Python’s built-in libraries.

Make sure Python 3 is installed:

```bash
python3 --version

If it's not installed, you can install it using
sudo apt update
sudo apt install python3
## How to run
git clone https://github.com/Dolapotheethicalhacker/Port-Scanner.git
cd Port-Scanner
python3 portscanner.py
Follow the prompts:

Enter your target IP or domain (e.g., scanme.nmap.org)

Wait for the scan to complete — open ports will be printed in the output.

Example output:

[+] Open port: 22
[+] Open port: 80
[+] Open port: 443
 Important Notes
Port scanning can be legally sensitive. Always obtain explicit permission before scanning devices or networks that you do not own or control.

This script does not perform service detection, OS fingerprinting, or UDP scanning — it's strictly for TCP port checking.

Ideal for small-scale scans and educational purposes. For enterprise-grade scanning, consider using tools like Nmap or Masscan.

The default range is ports 1–1024. You can modify the script to scan all 65535 ports or a custom range.

On Linux or macOS, you may need to run the script with sudo to avoid permission issues when scanning certain ports.

 Customization Tips
 Custom Port Ranges: Modify the range(1, 1025) line to scan specific ranges.

 Timeout Settings: Adjust socket timeout for more/less aggressive scanning.

 Save Output to File: Redirect output or write open ports to a log file.

 Add Banner Grabbing: Use socket recv methods to grab banners from open services.

 Developed By
Dolapotheethicalhacker — A cybersecurity enthusiast, ethical hacker, and Python programmer passionate about making security tools accessible and beginner-friendly.


 Disclaimer: This tool is provided for educational purposes only. The developer is not responsible for any misuse. Always follow ethical hacking guidelines and local laws.


## Created by DolapotheEthicalHacker

