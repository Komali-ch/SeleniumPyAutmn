from selenium.webdriver.common.by import By


class ApplicationPage:
    langset_xpath = "(//i[@role='img'])[3]"
    theme_xpath   = "(//i[@role='img'])[4]"
    hindi_xpath  = "//label[2]//div[2]//div[1]//div[1]"
    spanish_xpath = "//label[3]//div[2]//div[1]//div[1]"
    # langslist_xpath = "//div[@class='q-mt-xs q-mb-sm q-list']"
    # langslist_xpath = "//input[@type='radio' and @class='hidden q-radio__native q-ma-none q-pa-none']"
    about_lnktxt = "About"
    legal_lnktxt = "Legal"

    def __init__(self, driver):
        self.driver = driver

    def modifyTheme(self):
        self.driver.find_element(By.XPATH, self.theme_xpath).click()

    def langSet(self):
        self.driver.find_element(By.XPATH, self.langset_xpath).click()

    def langSet2(self):
        self.driver.find_element(By.XPATH, self.hindi_xpath).click()

    def langSet3(self):
        self.driver.find_element(By.XPATH, self.spanish_xpath).click()

    # def langList(self):
    #     self.driver.find_elements(By.XPATH, self.langs2_xpath).click()

    def aboutLnk(self):
        self.driver.find_element(By.LINK_TEXT, self.about_lnktxt).click()

    def legalLnk(self):
        self.driver.find_element(By.LINK_TEXT, self.legal_lnktxt).click()
