from scapy.all import *
import random

# Define the target IPs and ports to scan
targets = ["172.31.9.102", "172.31.9.187"]
ports = [22, 80, 443]  # A sample set of ports

# Function to perform SYN scan
def syn_scan(target, ports):
    for port in ports:
        # Create SYN packet
        ip = IP(dst=target)
        syn = TCP(dport=port, flags="S", seq=random.randint(1000, 10000))
        syn_packet = ip / syn

        # Send the SYN packet and capture the response
        response = sr1(syn_packet, timeout=1, verbose=0)
        print(f"{response}")
        if response:
            # Check the flags in the response
            if response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK means port is open
                    print(f"[+] Open port {port} on {target} - Flags: SYN-ACK")
                elif response.getlayer(TCP).flags == 0x14:  # RST-ACK means port is closed
                    pass
        else:
            print(f"[-] No response from {target} on port {port}")

# Perform the scan for each target
for target in targets:
    print(f"Scanning {target}...")
    syn_scan(target, ports)
