from selenium.webdriver.common.by import By


class Login:
    # username_xpath = "//*[text()='Email or Phone']"
    username_xpath = "//input[@aria-label='Email or Phone']"
    password_xpath = "//input[@type='password']"
    login_xpath = "//span[contains(text(),'Sign in')]"

    def __init__(self, driver):
        self.driver = driver

    def setUsrname(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def clkLgn(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()
