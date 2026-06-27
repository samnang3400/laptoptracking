import os
import ctypes
import subprocess

def execute_command(cmd):
    """Execute a remote command (lock, shutdown, restart)."""
    cmd_type = cmd['type']
    result = ""
    success = False
    
    try:
        if cmd_type == 'lock':
            ctypes.windll.user32.LockWorkStation()
            result = "Workstation locked"
            success = True
            
        elif cmd_type == 'shutdown':
            # Give user 10 seconds to save work
            os.system("shutdown /s /t 10 /c \"Remote shutdown initiated by IT\"")
            result = "Shutdown initiated (10s delay)"
            success = True
            
        elif cmd_type == 'restart':
            os.system("shutdown /r /t 10 /c \"Remote restart initiated by IT\"")
            result = "Restart initiated (10s delay)"
            success = True
            
        else:
            result = f"Unknown command type: {cmd_type}"
            success = False
            
    except Exception as e:
        result = str(e)
        success = False
        
    return success, result
