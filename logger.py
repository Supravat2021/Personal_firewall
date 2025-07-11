from datetime import datetime

def log_suspicious(packet, reason=""):
    with open("firewall_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] ❌ BLOCKED | {reason} | {packet.summary()}\n")

def log_allowed(packet):
    with open("firewall_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] ✅ ALLOWED | {packet.summary()}\n")
