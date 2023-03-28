from MobileAutomation2.Utils import Contacts
obj = Contacts.Contacts()
obj.lockScreen()
obj.swipeUp()
#[0,1300][720,1448]

#[49,100][672,259]
#subprocess.call("adb shell input touchscreen swipe 500 450 350 1350")
#subprocess.call("adb shell input touchscreen swipe 25 500 200 1350")

obj.launchContactui()
obj.pressBack()