from PageObjects.Login_Page import Login
# from Selenium.PageObjects.Login_Page import Addcust_Custrole
from Utilities.CustomerLogger import LogGen
# from Selenium.Alerts_Pops.Alerts_Popups import alerts_Popups
from selenium import webdriver
import time
# from Selenium.TestCases.Confitest import pytest_configure
import random
import string
import pytest

# from selenium.webdriver.common.by import By

class Test_001_Login:
        Url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
        username = "admin@yourstore.com"
        password = "admin"
        # Email = "Shaik.Fazz@gmail.com"
        Passwrd = "Fazz@9786"
        logger = LogGen.Loggen()

        def test_homepageTitle(self):
                self.logger.info("****************************  Login TestCase One Started****************************")
                self.driver = webdriver.Chrome()
                self.driver.get(self.Url)
                self.driver.maximize_window()
                # time.sleep(5)
                get_title = self.driver.title
                self.driver.close()
                if get_title == "Your store. Login":
                    assert True
                else:
                    assert False
                self.logger.info("**************************** Login TestCase One Completed***************************")

        def test_login(self):
                self.logger.info("********************* Second TestCase Started***************************************")
                self.driver = webdriver.Chrome()
                self.driver.get(self.Url)
                self.driver.maximize_window()
                self.p = Login(self.driver)
                self.logger.info("***************************** Login Successful *************************************")
                time.sleep(3)
                self.p.username(self.username)
                time.sleep(3)
                self.p.password(self.password)
                time.sleep(2)
                self.p.Login()
                get_title = self.driver.title
                if get_title == "Dashboard / nopCommerce administration":
                        assert True
                else:
                        assert False

        def test_AddingCustomers(self):
                self.driver = webdriver.Chrome()
                self.driver.get(self.Url)
                self.driver.maximize_window()
                self.lp = Login(self.driver)
                self.lp.username(self.username)
                self.lp.password(self.password)
                self.lp.Login()
                self.lp.M_Customers()
                time.sleep(5)
                self.lp.customers()
                self.lp.Add_New()
                ###### Method to create random email's
                def random_generator(size=20, char=string.ascii_lowercase + string.digits):
                        return "".join(random.choice(char) for x in range(size))
                self.email = random_generator() +"@gamil.com"
                self.lp.Add_Email(self.email)
                time.sleep(5)
                self.lp.Add_Passwrd(self.Passwrd)
                time.sleep(5)
                self.driver.execute_script("window.scrollBy(0,500)")
                self.lp.Add_FirstName("Shaik")
                self.lp.Add_LastName("Fazz")
                time.sleep(5)
                self.lp.Selecting_Gender()
                time.sleep(5)
                self.lp.Selecting_Vendor("Vendor 1")
                time.sleep(5)
                self.driver.close()


