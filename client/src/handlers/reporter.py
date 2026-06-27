import requests
import json

def send_report(server_url, api_key, report_data):
    """POST the collected data to the server."""
    try:
        headers = {
            'X-API-Key': api_key,
            'Content-Type': 'application/json'
        }
        resp = requests.post(
            f"{server_url}/api/report",
            json=report_data,
            headers=headers,
            timeout=10
        )
        return resp.status_code == 200
    except Exception as e:
        print(f"Report error: {e}")
        return False
