import subprocess
from pynput import keyboard

def on_press(key):
    try: k = key.char
    except AttributeError: k = key.name
    if k == 'page_down':
        print('Key pressed: ' + k)
        subprocess.check_output(['netsh interface set interface Wi-Fi enable'])
        subprocess.check_output(['netsh interface set interface Ethernet disable'])
    elif k == 'page_up':
        print('Key pressed: ' + k)
        subprocess.check_output(['netsh interface set interface Ethernet enable'])
        subprocess.check_output(['netsh interface set interface Wi-Fi disable'])

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys
