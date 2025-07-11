import tkinter as tk
import subprocess
import os

firewall_process = None

def start_firewall():
    global firewall_process
    if firewall_process is None:
        firewall_process = subprocess.Popen(["sudo", "python3", "firewall.py"])
        status_label.config(text="🟢 Firewall is RUNNING", fg="green")
    else:
        status_label.config(text="⚠️ Already running", fg="orange")

def stop_firewall():
    global firewall_process
    if firewall_process:
        firewall_process.terminate()
        firewall_process.wait()
        firewall_process = None
        status_label.config(text="🔴 Firewall is STOPPED", fg="red")
    else:
        status_label.config(text="⚠️ Not running", fg="orange")

def clear_log():
    try:
        open("firewall_log.txt", "w").close()  # Clears the file
        log_display.delete(1.0, tk.END)
        log_display.insert(tk.END, "✅ Log cleared.\n")
    except Exception as e:
        log_display.insert(tk.END, f"❌ Error clearing log: {e}\n")

def update_log():
    log_path = os.path.abspath("firewall_log.txt")
    try:
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                logs = f.readlines()
            logs.reverse()  # ⬅️ Reverse the lines
            logs = "".join(logs)
        else:
            logs = "No logs yet..."
    except Exception as e:
        logs = f"❌ Error reading log: {e}"

    log_display.delete(1.0, tk.END)
    log_display.insert(tk.END, logs)
    root.after(3000, update_log)


# GUI Setup
root = tk.Tk()
root.title("🔥 Personal Firewall GUI")
root.geometry("1000x650")

status_label = tk.Label(root, text="🔴 Firewall is STOPPED", font=("Arial", 14, "bold"), fg="red")
status_label.pack(pady=10)

# Buttons: Start, Stop, Clear Log
button_frame = tk.Frame(root)
button_frame.pack()

start_btn = tk.Button(button_frame, text="Start Firewall", command=start_firewall,
                      bg="green", fg="white", font=("Arial", 12), padx=10)
start_btn.pack(side="left", padx=10)

stop_btn = tk.Button(button_frame, text="Stop Firewall", command=stop_firewall,
                     bg="red", fg="white", font=("Arial", 12), padx=10)
stop_btn.pack(side="left", padx=10)

clear_btn = tk.Button(button_frame, text="Clear Log", command=clear_log,
                      bg="orange", fg="black", font=("Arial", 12), padx=10)
clear_btn.pack(side="left", padx=10)

# Log Display
log_display = tk.Text(root, height=28, width=120, bg="black", fg="white", font=("Courier", 10))
log_display.pack(padx=10, pady=10)

update_log()
root.mainloop()
