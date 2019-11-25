import subprocess
from pynput import keyboard

# TODO
# Install python
# pip install pynput
# wmic nic get name, index

def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if k == 'page_down': # keys interested
        print('Key pressed: ' + k)
        subprocess.check_output('netsh interface set interface Wi-Fi enable')
        subprocess.check_output('netsh interface set interface Ethernet disable')
    elif k == 'page_up': # keys interested
        print('Key pressed: ' + k)
        subprocess.check_output('netsh interface set interface Ethernet enable')
        subprocess.check_output('netsh interface set interface Wi-Fi disable')

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys
