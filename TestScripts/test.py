import subprocess

from uiautomator import Device
import time

d = Device("BAYDZPJ7559DK7CU")
#subprocess.call("adb shell input touchscreen swipe 930 880 830 380")
#d.press.back()

#time.sleep(3)
d(text="Contacts").click()
time.sleep(3)
d.press.back()
time.sleep(2)
d.press.home()




