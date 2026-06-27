import socket
import subprocess
import re
import requests

def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return '0.0.0.0'

def get_public_ip():
    try:
        resp = requests.get('https://api.ipify.org', timeout=5)
        return resp.text.strip()
    except:
        return None

def get_wifi_ssid():
    """Windows only - uses netsh."""
    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'interfaces'],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        match = re.search(r"SSID\s*:\s(.+)", result.stdout)
        return match.group(1).strip() if match else None
    except:
        return None
