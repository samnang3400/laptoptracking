import sys
import time
import json
import socket

# Add project root to path for imports
sys.path.append(sys.path[0])

from core.identity import get_client_id
from core.config_loader import load_config
from collectors.system import get_user, get_hostname
from collectors.network import get_local_ip, get_public_ip, get_wifi_ssid
from collectors.browser import get_active_browser_tab
from handlers.reporter import send_report
from handlers.commander import execute_command
from handlers.result_reporter import report_result

def build_report(client_id):
    """Gather all data into a single dict."""
    return {
        "client_id": client_id,
        "timestamp": time.time(),
        "user": get_user(),
        "hostname": get_hostname(),
        "local_ip": get_local_ip(),
        "public_ip": get_public_ip(),
        "ssid": get_wifi_ssid(),
        "browser": get_active_browser_tab()
    }

def fetch_command(server_url, api_key, client_id):
    """Ask the server if there's a pending command."""
    try:
        headers = {'X-API-Key': api_key}
        resp = requests.get(
            f"{server_url}/api/commands",
            params={"client_id": client_id},
            headers=headers,
            timeout=10
        )
        if resp.status_code == 200:
            data = resp.json()
            if "command_id" in data:
                return data
    except Exception as e:
        print(f"Command fetch error: {e}")
    return None

def main():
    print("🚀 Starting Laptop Monitor Agent...")
    config = load_config()
    server_url = config['server_url']
    api_key = config['api_key']
    poll_interval = config['poll_interval']
    client_id = get_client_id()
    
    print(f"Client ID: {client_id}")
    print(f"Server: {server_url}")
    print(f"Poll interval: {poll_interval}s")
    
    while True:
        try:
            # 1. Send system report
            report = build_report(client_id)
            success = send_report(server_url, api_key, report)
            if success:
                print(f"[{time.strftime('%H:%M:%S')}] Report sent successfully.")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] Report failed.")
            
            # 2. Check for commands
            cmd = fetch_command(server_url, api_key, client_id)
            if cmd:
                print(f"Received command: {cmd['type']}")
                success, result_msg = execute_command(cmd)
                report_result(server_url, api_key, cmd['command_id'], success, result_msg)
                print(f"Command result: {result_msg}")
                
        except Exception as e:
            print(f"Main loop error: {e}")
            
        time.sleep(poll_interval)

if __name__ == "__main__":
    # Import requests here to avoid circular issues
    import requests
    main()
