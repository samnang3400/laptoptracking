import win32gui
import win32process
import psutil

def get_active_browser_tab():
    """Get the foreground window's process and title if it's a browser."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        if not hwnd:
            return None
        
        title = win32gui.GetWindowText(hwnd)
        if not title:
            return None
            
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proc = psutil.Process(pid)
        proc_name = proc.name().lower()
        
        browsers = ['chrome.exe', 'msedge.exe', 'firefox.exe', 'opera.exe', 'brave.exe']
        if any(b in proc_name for b in browsers):
            return {
                "browser": proc_name,
                "title": title
            }
    except Exception:
        pass
    return None
