from selenium.webdriver.common.by import By
from pages.LoginPage import Login
import time


class Test_u02_Verify_subheader_menu:
    webappUrl = 'https://dev.usync.us/'
    username = 'Rahul456@gmail.com'
    password = 'Rahul@1234'

    def test_00_click_on_all_subheader_menu_options(self, setup):
        driver = setup
        driver.get(self.webappUrl)
        driver.maximize_window()

        lgnp = Login(driver)
        lgnp.setUsrname(self.username)
        lgnp.setPassword(self.password)
        lgnp.clkLgn()
        time.sleep(5)
        submenu_options = driver.find_elements(By.XPATH,
                                               "//label[@class='footnote footnote--bold text-color-3 clickable']")
        for menu in submenu_options:
            menu.click()

        print(len(submenu_options))
