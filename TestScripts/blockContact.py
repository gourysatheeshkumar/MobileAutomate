from MobileAutomation2.Utils import Contacts
import time
obj = Contacts.Contacts()

obj.launchContactui()
obj.BlockContacts()
obj.pressBack2()
obj.pressBack()
obj.lockScreen()
