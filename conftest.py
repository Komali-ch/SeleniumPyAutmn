from selenium import webdriver
import  pytest

# This particular decorator will make this method as a fixture
# Whenever we call the fixture it will return the driver
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32_V104\chromedriver.exe")
    return driver

# Instead of creation driver multiple times, created conftest file
