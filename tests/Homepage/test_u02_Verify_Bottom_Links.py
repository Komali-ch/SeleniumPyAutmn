from pages.WebapphomePage import ApplicationPage
from utilities.readProperties import ReadConfig
import time


class Test_u02_Verify_bottom_links:
    webappUrl = 'https://dev.usync.us/'

    def test_00_click_bottom_links(self, setup):
        driver = setup
        driver.get(self.webappUrl)
        # driver.maximize_window()
        driver.execute_script("window.scrollBy(0,100)", "")
        about = ApplicationPage(driver)
        about.aboutLnk()
        time.sleep(3)
        windowIds = driver.window_handles
        driver.switch_to.window(windowIds[0])
        about.legalLnk()
        time.sleep(5)
        driver.quit()
