import os

def block_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")

def block_port(port):
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")
