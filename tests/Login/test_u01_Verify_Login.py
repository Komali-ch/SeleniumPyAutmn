from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.LoginPage import Login
import time


class Test_u01_Verify_title_login:
    webappUrl = 'https://dev.usync.us/'
    username = 'Rahul456@gmail.com'
    password = 'Rahul@1234'
# We should not hard code data in test cases
# if suppose value changes  then needs to go every tc and modify instead of that keep the common data in one file
# To read data from config.ini file, need some utility file - Reusability

    def test_00_verify_captured_title(self, setup):
        self.driver = setup
        self.driver.get(self.webappUrl)
        self.driver.maximize_window()
        act_title = self.driver.title
        exp_title = "uSync App"
        if act_title == exp_title:
            print("Application launched successfully")
        else:
            print("Appn launch failed")

    def test_01_application_log_in(self, setup):
       self.driver = setup
       wait = WebDriverWait(self.driver, 5, ignored_exceptions=Exception)
       self.driver.get(self.webappUrl)
       self.ul = Login(self.driver)
       # wait.until(EC.presence_of_element_located(self.ul.setUsrname(self.username)))
       self.ul.setUsrname(self.username)
       # time.sleep(2)
       self.ul.setPassword(self.password)
       self.ul.clkLgn()
       self.driver.close()

