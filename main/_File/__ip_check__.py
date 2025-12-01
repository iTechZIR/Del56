# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c
# this code is for windows "Linux" version will be released soon

import socket
import threading
from datetime import datetime
import requests
import json
import psutil
from concurrent.futures import ThreadPoolExecutor

class ConnectionMonitor:
    def __init__(self):
        self.logfile = 'main/_Logging/__connection-monitor__.txt'
        self.monitored_ports = set()

    def _get_ip_info(self, ipaddress):
        try:
            response = requests.get(f'http://ip-api.com/json/{ipaddress}?fields=status,country,city', timeout=5)
            data = response.json()

            if data.get('status') == 'success':
                country = data.get('country', 'N/A')
                city = data.get('city', 'N/A')
                return f"{country}/{city}"
            else:
                return "Unknown/Unknown"

        except Exception:
            return "Unknown/Unknown"

    def _log_connection(self, localport, remoteip, remoteport, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        location = self._get_ip_info(remoteip)
        logmessage = f"[{timestamp}] - LOCAL:{localport} <- {remoteip}:{remoteport} - {location} - {status}"
        print(logmessage)

        with open(self.logfile, 'a', encoding='utf-8') as f:
            f.write(logmessage + '\n')

    def _monitor_all_connections(self):
        while True:
            try:
                connections = psutil.net_connections(kind='inet')
                
                for conn in connections:
                    if conn.status == 'ESTABLISHED' and conn.laddr and conn.raddr:
                        localport = conn.laddr.port
                        remoteip = conn.raddr.ip
                        remoteport = conn.raddr.port
                        
                        if localport not in self.monitored_ports:
                            self.monitored_ports.add(localport)
                            self._log_connection(localport, remoteip, remoteport, "NEW_CONNECTION")
                        
            except Exception as e:
                print(f"-  Monitoring error: {e}")
            
            threading.Event().wait(2)  

    def _start_monitoring(self):
        print("=" * 53)
        print("-  connection monitor starting . . .")
        print(f"-  logging to: {self.logfile}")
        print("=" * 53)
        print()

        monitorthread = threading.Thread(target=self._monitor_all_connections)
        monitorthread.daemon = True
        monitorthread.start()

        try:
            while True:
                threading.Event().wait(1)
        except KeyboardInterrupt:
            print("\n-  stopping monitor . . .")

def main():
    monitor = ConnectionMonitor()
    monitor._start_monitoring()

if __name__ == "__main__":
    main()
