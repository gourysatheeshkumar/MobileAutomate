from MobileAutomation2.Utils import Contacts
import time
obj = Contacts.Contacts()

obj.launchContactui()

obj.editContact()
obj.editMoreName()
obj.clickOnFirstName()
obj.editName()
obj.saveContact()
obj.pressBack2()
obj.pressBack()
obj.lockScreen()