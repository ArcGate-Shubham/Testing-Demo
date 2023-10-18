import pytest
from selenium import webdriver
driver = None
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)
    request.cls.driver.get(config.get("Url","base_url"))
    yield
    request.cls.driver.quit()
