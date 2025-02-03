import socket
import threading
import subprocess
import re
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MetaScope:
    def __init__(self, root):
        self.root = root
        self.root.title("MetaScope - Network Device Mapper")
        self.devices = []

        self.setup_gui()

    def setup_gui(self):
        self.tree = ttk.Treeview(self.root, columns=("IP", "MAC", "Hostname"), show="headings")
        self.tree.heading("IP", text="IP Address")
        self.tree.heading("MAC", text="MAC Address")
        self.tree.heading("Hostname", text="Hostname")
        self.tree.pack(expand=True, fill=tk.BOTH)

        scan_button = ttk.Button(self.root, text="Scan Network", command=self.scan_network)
        scan_button.pack(pady=10)

    def scan_network(self):
        self.devices.clear()
        self.tree.delete(*self.tree.get_children())

        ip_list = self.get_local_ip_range()
        threads = []

        for ip in ip_list:
            thread = threading.Thread(target=self.ping_device, args=(ip,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.display_devices()

    def get_local_ip_range(self):
        local_ip = socket.gethostbyname(socket.gethostname())
        ip_parts = local_ip.split('.')
        base_ip = '.'.join(ip_parts[:3])
        return [f"{base_ip}.{i}" for i in range(1, 255)]

    def ping_device(self, ip):
        try:
            output = subprocess.check_output(['ping', '-n', '1', '-w', '500', ip], stderr=subprocess.DEVNULL, universal_newlines=True)
            if "TTL=" in output:
                hostname = self.get_hostname(ip)
                mac = self.get_mac_address(ip)
                self.devices.append((ip, mac, hostname))
        except subprocess.CalledProcessError:
            pass

    def get_hostname(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"

    def get_mac_address(self, ip):
        try:
            pid = subprocess.Popen(["arp", "-a", ip], stdout=subprocess.PIPE)
            output = pid.communicate()[0].decode('utf-8')
            mac_address = re.search(r"(([a-f\d]{1,2}-){5}[a-f\d]{1,2})", output, re.I).groups()[0]
            return mac_address
        except:
            return "Unknown"

    def display_devices(self):
        for device in self.devices:
            self.tree.insert("", tk.END, values=device)
        messagebox.showinfo("Scan Complete", "Network scan completed successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetaScope(root)
    root.geometry("600x400")
    root.mainloop()