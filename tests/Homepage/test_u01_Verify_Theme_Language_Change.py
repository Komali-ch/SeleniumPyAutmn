import time
from pages.WebapphomePage import ApplicationPage


class Test_u01_Verify_theme_language_change:
    webappUrl = 'https://dev.usync.us/'

    def test_00_verify_theme_change(self, setup):
        driver = setup
        driver.get(self.webappUrl)
        themelng = ApplicationPage(driver)
        themelng.modifyTheme()
        themelng.langSet()
        time.sleep(5)
        themelng.langSet2()
        time.sleep(5)
        themelng.langSet3()
        driver.close()
