from selenium.webdriver.common.by import By


class NavigationPage:
    refine_xpath = "//i[@class='q-tab__icon q-icon fal fa-sliders-h']"
    rfnbck_xpath = "//div[@class='app-panel items-stretch hide-scrollbar__panel app-panel--tab-panels refine--xs app-panel--indicator-bottom app-panel--standard']" \
                   "//div[@class='row items-center']//div[1][1]//i[1]"
    search_xpath = "//i[@class='q-tab__icon q-icon fal fa-search']"
    srchback_xpath = "(//i[@role='presentation'])[20]"
    startour_xpath = "(//i[@role='img'])[6]"
    subheader_xpath = "//div[@class='clickable']"

    def __init__(self, driver):
        self.driver = driver

    def refineClk(self):
        self.driver.find_element(By.XPATH, self.refine_xpath).click()

    def refineBack(self):
        self.driver.find_element(By.XPATH, self.rfnbck_xpath).click()

    def searchClk(self):
        self.driver.find_element(By.XPATH, self.search_xpath).click()

    def srchBack(self):
        self.driver.find_element(By.XPATH, self.srchback_xpath).click()

    def searchTour(self):
        self.driver.find_element(By.XPATH, self.startour_xpath).click()

    def subHeader(self):
        self.driver.find_elements(By.XPATH, self.subheader_xpath)
