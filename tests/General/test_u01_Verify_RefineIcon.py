from selenium import webdriver
from pages.NavigationsPage import NavigationPage
from pages.LoginPage import Login
from utilities.readProperties import ReadConfig
import time


class Test_u02_Verify_refineIcon_click:
    # ops = webdriver.ChromeOptions()
    # ops.add_argument("--disable-notifications")
    webappUrl = 'https://dev.usync.us/'
    username = 'Rahul456@gmail.com'
    password = 'Rahul@1234'

    # webappUrl = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getPassword()

    def test_00_click_on_topright_options(self, setup):
        driver = setup
        driver.get(self.webappUrl)
        driver.maximize_window()

        lgnp = Login(driver)
        lgnp.setUsrname(self.username)
        # time.sleep(2)
        lgnp.setPassword(self.password)
        lgnp.clkLgn()
        time.sleep(5)
        refine = NavigationPage(driver)
        # 1st option
        refine.searchClk()
        time.sleep(3)
        refine.srchBack()
        time.sleep(2)
        # 2nd option
        refine.refineClk()
        time.sleep(6)
        refine.refineBack()
        time.sleep(2)
        # 3rd option
        refine.searchTour()
        time.sleep(2)
