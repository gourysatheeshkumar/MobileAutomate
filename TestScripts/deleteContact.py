from MobileAutomation2.Utils import Contacts
import time
obj = Contacts.Contacts()

obj.launchContactui()
obj.deleteContact()
obj.pressBack2()
obj.lockScreen()