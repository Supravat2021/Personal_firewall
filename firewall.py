from scapy.all import sniff, IP, TCP, UDP
from logger import log_suspicious, log_allowed
import json
import os
import subprocess

with open("rules.json", "r") as f:
    rules = json.load(f)

# Function to apply iptables block
def block_ip(ip):
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], stderr=subprocess.DEVNULL)
    subprocess.run(["iptables", "-A", "OUTPUT", "-d", ip, "-j", "DROP"], stderr=subprocess.DEVNULL)

def block_port(port):
    subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"], stderr=subprocess.DEVNULL)
    subprocess.run(["iptables", "-A", "OUTPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"], stderr=subprocess.DEVNULL)

def packet_filter(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"
        port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else None

        if src_ip in rules['deny_ips']:
            log_suspicious(packet, "Denied Source IP")
            block_ip(src_ip)

        elif dst_ip in rules['deny_ips']:
            log_suspicious(packet, "Denied Destination IP")
            block_ip(dst_ip)

        elif port in rules['deny_ports']:
            log_suspicious(packet, f"Denied Port {port}")
            block_port(port)

        elif proto not in rules['protocols']:
            log_suspicious(packet, "Unknown Protocol")

        else:
            log_allowed(packet)

sniff(filter="ip", prn=packet_filter, store=0)
