import configparser
import os

def load_config():
    config = configparser.ConfigParser()
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = os.path.join(base_dir, 'config.ini')
    config.read(config_path)
    
    return {
        "server_url": config.get('DEFAULT', 'SERVER_URL'),
        "api_key": config.get('DEFAULT', 'API_KEY'),
        "poll_interval": config.getint('DEFAULT', 'POLL_INTERVAL')
    }
