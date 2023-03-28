from MobileAutomation2.Libraries import adbLibrary
from MobileAutomation2.Libraries import uiLibrary
import time

from MobileAutomation2.Resources.TestData import mydata
obj1 = adbLibrary.adbLibrary()
obj2 = uiLibrary.uiLibrary()

class Contacts():
    def __init__(self):
        pass
    def launchContact(self):
        #obj1.launchApp("com.android.contacts/.activities.PeopleActivity")
        obj1.launchApp(mydata["contactsPkname"])
    def launchContactui(self):
        obj2.clickOnText("Contacts")

    def clickOnContacts(self):
        obj2.clickOnContacts()
    def clickOnPlus(self):
        obj2.clickOnPlus()
    def clickOnFullName(self):
        obj2.clickOnFullName()
        obj1.pressBack()
    def clickOnFirstName(self):
        obj2.clickOnFirstName()
    def nameEntryAdb(self):
        obj1.nameEntryAdb()
    def clickOnMobile(self):
        obj2.clickOnMobile()
    def phoneNumberEntryAdb(self):
        obj1.phoneNumberEntryAdb()
    def saveContact(self):
        obj2.saveContact()
    def editContact(self):
        obj2.editContact()
    def editContact1(self):
        obj2.editContact1()
    def editName(self):
        obj1.editName()
    def editMoreName(self):
        obj2.editMoreName()
        time.sleep(2)
    def pressBack(self):
        obj1.pressBack()
    def deleteContact(self):
        obj2.deleteContact()

    def seltoBlock(self):
        obj2.seltoBlock()

    def blockContact(self):
        obj2.blockContact()
    def BlockContacts(self):
        obj2.BlockContacts()

    def unBlockContacts(self):
        obj2.unBlockContacts()

    def selContacttoUnblock(self):
        obj2.selContacttoUnblock()

    def unBlockContact(self):
        obj2.unBlockContact()

    def selForMore(self):
        obj2.selForMore()
    def swipeUp(self):
        obj1.swipeUp()
    def lockScreen(self):
        obj1.lockScreen()
    def pressBack2(self):
        obj2.pressBack2()