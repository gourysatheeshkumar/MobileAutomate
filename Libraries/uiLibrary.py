from uiautomator import Device
import time

class uiLibrary():
    def __init__(self):
        self.d = Device('BAYDZPJ7559DK7CU')
        pass
    def clickOnText(self, textName):
        self.d(text=textName).click()
        time.sleep(2)

        # if self.d(text="Contacts").exists:
        #     print("Contact launched is successfully")
        # else:
        #     print("Contact launched is unsuccessfully")

    def clickOnContacts(self): #click on contacts
        self.d(resourceId="com.google.android.contacts:id/navigation_bar_item_icon_view").click()
    def clickOnPlus(self):
        self.d(resourceId="com.google.android.contacts:id/floating_action_button").click()

    def clickOnFullName(self):
        self.d(text="First name").click()
        time.sleep(2)
        #self.d.press.back()
    def clickOnFirstName(self):
        self.d(text="sisi").click()
        time.sleep(2)

    def clickOnMobile(self):
        self.d(className="android.widget.EditText", instance=3).click()
        time.sleep(2)
    def saveContact(self): #[448,80][624,176]
        self.d.click(550, 130)
        time.sleep(2)
    def editContact(self):
        self.d(text="sisi").click()
        time.sleep(2)
    def editContact1(self):
        self.d(text="sisindri").click()
        time.sleep(2)
    #[107,1872][163,1912]
    def editMoreName(self):
        #self.d.click(130,1900)
        #[432, 80][528, 176]
        self.d.click(475,125)
    #[919,63][1038,168]
    # def clickOnMobile(self):
    #     self.d(700,700).click()

    def pressBack(self):
        self.d.press.back()
    def pressBack2(self):
        for i in range(2):
            self.d.press.back()
            time.sleep(2)

    #[913, 1798][976, 1861]
    def deleteContact(self):
        self.d(text="sisindri").click()  # select contacts
        time.sleep(2)
        #self.d.click(950,1830)
        #[624, 80][720, 176]
        self.d.click(660,120)
        time.sleep(2)
        self.d(text="Delete").click()
        time.sleep(2)
        self.d(text="Delete").click()
        time.sleep(2)

    def BlockContacts(self):
        self.d(text="sisindri").click()  # select contacts
        time.sleep(2)
        #self.d.click(950,1830)
        #[624, 80][720, 176]
        self.d.click(660,120)
        time.sleep(2)
        self.d(text="Block numbers").click()
        time.sleep(2)
        self.d(text="Block").click()
        time.sleep(2)

    def unBlockContacts(self):
        self.d(text="sisindri").click()  # select contacts
        time.sleep(2)
        #self.d.click(950,1830)
        #[624, 80][720, 176]
        self.d.click(660,120)
        time.sleep(2)
        self.d(text="Unblock numbers").click()
        time.sleep(2)
        self.d(text="Unblock").click()
        time.sleep(2)

    def seltoBlock(self):
        self.d(text="sisindri").click()
        time.sleep(2)

    def blockContact(self):
        self.d.click(950, 1830)
        self.d(text="Add to blacklist").click()
        time.sleep(2)
        self.d(text="Add to blacklist").click()
        time.sleep(2)

    def selContacttoUnblock(self):
        self.d(text="sisindri").click()  # select contacts
        time.sleep(2)

    def unBlockContact(self):
        self.d.click(950, 1830)
        self.d(text="Unblock").click()
        self.d(text="Unblock").click()
        time.sleep(2)

    def selForMore(self):
        self.d(text="sisindri").click()
        time.sleep(2)