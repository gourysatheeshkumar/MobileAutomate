import subprocess
import time

class adbLibrary():
    def __init__(self):
        subprocess.check_output("adb devices")
        pass
    def launchApp(self,apkName):
        subprocess.run(['adb','shell','am','start','-n', apkName])
        print("apk started successfully")
    def nameEntryAdb(self):
        subprocess.run("adb shell input text sisi", shell=True)
        time.sleep(2)
        subprocess.run("adb shell input keyevent 4")
    def phoneNumberEntryAdb(self):
        subprocess.run("adb shell input text 9100359527")
    def editName(self):
        subprocess.run("adb shell input text ndri")
        time.sleep(2)
    def pressBack(self):
        subprocess.run("adb shell input keyevent 4")
    def swipeUp(self):
        #subprocess.call("adb shell input touchscreen swipe 500 450 350 1350")
        #subprocess.call("adb shell input touchscreen swipe 930 880 830 380")
        subprocess.call("adb shell input touchscreen swipe 25 500 200 1350")
        #time.sleep(2)
        #[0,1300][720,1448]

    def lockScreen(self):
        subprocess.call("adb shell input keyevent 26")