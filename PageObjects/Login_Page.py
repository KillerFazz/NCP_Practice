import time

from selenium.webdriver.common.by import By
# from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Login:
    Username_textbox = '//*[@id="Email"]'
    Password_textbox = '//input[@id="Password"]'
    Login_button = '//button[@class="button-1 login-button"]'
    Logout_button = '//*[@id="navbarText"]/ul/li[3]/a'
    Menu_Customers = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    Customers = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    Adding_New_Coustmer = '//*[@class="btn btn-primary"]'
    textbox_Email_ID = "Email"
    input_password = '//input[@id="Password"]'
    firstname_id = "FirstName"
    LastName_id ='LastName'
    Gender_id = 'Gender_Male'
    Vendor_Id = 'VendorId'


    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.XPATH, self.Username_textbox).clear()
        self.driver.find_element(By.XPATH, self.Username_textbox).send_keys(username)

    def password(self, passwrd):
        self.driver.find_element(By.XPATH, self.Password_textbox).clear()
        self.driver.find_element(By.XPATH, self.Password_textbox).send_keys(passwrd)

    def Login(self):
        self.driver.find_element(By.XPATH, self.Login_button).click()

    def Logout(self):
        self.driver.find_element(By.XPATH, self.Logout_button).click()

    def M_Customers(self):
        self.driver.find_element(By.XPATH, self.Menu_Customers).click()

    def customers(self):
        self.driver.find_element(By.XPATH, self.Customers).click()

    def Add_New(self):
        self.driver.find_element(By.XPATH, self.Adding_New_Coustmer).click()

    def Add_Email(self, email):
        self.driver.find_element(By.ID, self.textbox_Email_ID).send_keys(email)

    def Add_Passwrd(self, password):
        self.driver.find_element(By.XPATH, self.input_password).send_keys(password)

    def Add_FirstName(self, firstname):
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def Add_LastName(self, Lastname):
        self.driver.find_element(By.ID, self.LastName_id).send_keys(Lastname)

    def Selecting_Gender(self):
        self.driver.find_element(By.ID, self.Gender_id).click()


    CustomerRoles_XPATH = '//*[@id="customer-info"]/div[2]/div[11]/div[2]/div/div[1]/div/div'
    ListitemRegistered = '//*[@id="9710300f-7eea-4949-8058-f2360aa199a7"]'
    ListitemGuest = '//*[@id="9710300f-7eea-4949-8058-f2360aa199a7"]'
    ListitemForumModeators = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[2]'
    ListitemAdministrator = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[1]'
    ListitemVendor = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]'

    def Add_CustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.CustomerRoles_XPATH).click()
        time.sleep(5)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemRegistered)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemAdministrator)
        elif role == "Guests":
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            time.sleep(2)
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemGuest)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemRegistered)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemVendor)
        elif role == "Forum Modeator":
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemForumModeators)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.ListitemRegistered)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def Selecting_Vendor(self, value):
        drp =Select(self.driver.find_element(By.ID, self.Vendor_Id))
        drp.select_by_visible_text(value)


