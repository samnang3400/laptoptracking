import requests

def report_result(server_url, api_key, command_id, success, result_message):
    """Send command execution result back to the server."""
    try:
        headers = {
            'X-API-Key': api_key,
            'Content-Type': 'application/json'
        }
        payload = {
            "command_id": command_id,
            "status": "done" if success else "failed",
            "result": result_message
        }
        resp = requests.post(
            f"{server_url}/api/command_result",
            json=payload,
            headers=headers,
            timeout=10
        )
        return resp.status_code == 200
    except Exception as e:
        print(f"Result report error: {e}")
        return False
