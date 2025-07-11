# 🔥 Personal Python Firewall for Kali Linux

A lightweight, real-time firewall built using Python and `iptables`, designed for **Kali Linux**. It provides a GUI to control firewall activity and live log viewing.

---

## 💡 Features

- 🔍 Real-time packet sniffing using Scapy
- 🚫 Rule-based blocking of IPs, ports, and protocols
- 🔐 Uses iptables for system-level blocking
- 📋 Live log view of allowed and blocked packets
- 🧠 Simple GUI to control start/stop and view logs
- 🔄 JSON file to customize rules easily

---

## 🛠️ Installation on Kali Linux

1. **Clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/personal-firewall.git
cd personal-firewall
````

2. **Install Scapy (if not installed already)**:

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install scapy
```

3. **Run the firewall GUI** with root permission:

```bash
sudo python3 main.py
```

---

## 📂 File Structure

* `main.py` – GUI app to control and monitor the firewall
* `firewall.py` – Core packet inspection using Scapy
* `iptables_blocker.py` – Utility to block IPs or ports via iptables
* `logger.py` – Handles all logging
* `rules.json` – Define your firewall rules
* `firewall_log.txt` – Log file (created after first run)

---

## ✍️ Modify Firewall Rules (`rules.json`) Based on Your Criteria

Example format:

```json
{
  "allow_ips": ["8.8.8.8"],
  "deny_ips": ["1.1.1.1"],
  "allow_ports": [443],
  "deny_ports": [23, 21, 80],
  "protocols": ["TCP", "UDP"]
}
```

---

## 📊 Log Output Example

Logs are saved to `firewall_log.txt`:

```
[2025-07-11 20:12:23] ✅ ALLOWED | IP / TCP 192.168.1.100:443 > ...
[2025-07-11 20:12:25] ❌ BLOCKED | Denied Port 80 | IP / TCP ...
```

---

## ⚠️ Important Notes

* 🔴 Must be run as `sudo` to use `iptables` and capture packets.
* 🔐 Tested on **Kali Linux** (2023.4 and later).
* 🔄 Logs are auto-updated every 3 seconds in the GUI.
* ✅ Click "Clear Log" in GUI to empty the log file.
