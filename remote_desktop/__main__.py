from pyautogui import press,write
print('imported pag')
import time
import subprocess
import pygetwindow as gw
import os

if __name__ == '__main__':
    # Launch MSTSC
    subprocess.Popen(["mstsc"])

    # Wait until the MSTSC window appears
    while not any("Remote Desktop Connection" in w.title for w in gw.getAllWindows()):
        time.sleep(0.1)  # Check every 100ms
    time.sleep(0.1)
    # Type the remote computer IP/hostname
    press("enter")

    # Wait until the login prompt appears
    while not any("Windows Security" in w.title or "Credentials" in w.title for w in gw.getAllWindows()):
        time.sleep(0.1)
    time.sleep(0.1)
    # Enter password
    write(os.environ['PW'])
    press("enter")

