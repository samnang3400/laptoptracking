import os
import socket

def get_user():
    """Get the currently logged-in Windows user."""
    try:
        return os.getlogin()
    except:
        return os.environ.get('USERNAME', 'Unknown')

def get_hostname():
    return socket.gethostname()
