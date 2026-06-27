import os
import json
import uuid

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'client_config.json')

def get_client_id():
    """Read or generate a persistent UUID for this laptop."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)['client_id']
        except:
            pass
    
    # Generate new ID
    cid = str(uuid.uuid4())
    with open(CONFIG_FILE, 'w') as f:
        json.dump({'client_id': cid}, f)
    return cid
