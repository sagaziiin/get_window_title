import sys

def get_window_name(wait=3):
    import win32gui
    import time
    time.sleep(wait)
    w=win32gui
    w_name = w.GetWindowText (w.GetForegroundWindow())
    return w_name

if len(sys.argv) >= 2:
    wait = int(sys.argv[1])
else:
    wait = 3
print(f'{get_window_name(wait)}')
input('Exit ...')