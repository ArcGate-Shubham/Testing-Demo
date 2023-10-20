import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard_data
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_correct_username_correct_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        db = dashboard_data(self.driver)
        log.info("TEST CASE, test_correct_username_correct_password")
        log.info("Test case starting")
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        time.sleep(3)
        if 'Dashboard' in db.dashboard():
            assert True
            log.info("Test case pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_incorrect_username_correct_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE test_incorrect_username_correct_password")
        log.info("Test case started")
        login.input_username(config.get("credential", "incorrect_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        time.sleep(3)
        if 'Invalid credentials' in login.invalid_msg():
            assert True
            log.info("Test case pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_correct_username_incorrect_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE test_correct_username_incorrect_password")
        log.info("Test case started")
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "incorrect_password"))
        login.click_login()
        time.sleep(3)
        if 'Invalid credentials' in login.invalid_msg():
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case failed")
            assert False

    def test_incorrect_username_incorrect_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE test_incorrect_username_incorrect_password")
        login.input_username(config.get("credential", "incorrect_username"))
        login.input_password(config.get("credential", "incorrect_password"))
        login.click_login()
        time.sleep(3)
        if 'Invalid credentials' in login.invalid_msg():
            assert True
            log.info("test case pass")
        else:
            log.critical("test case failed")
            assert False

    def test_blank_username_correct_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE test_blank_username_correct_password")
        log.info("Test Case started")
        login.input_username('')
        login.input_password('admin123')
        login.click_login()
        time.sleep(3)
        if 'Required' in login.invalid_required():
            assert True
            log.info("test case pass")
        else:
            log.critical("test case failed")
            assert False

    def test_correct_username_blank_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE test_correct_username_blank_password")
        login.input_username('Admin')
        login.input_password('')
        login.click_login()
        time.sleep(3)
        if 'Required' in login.invalid_required():
            assert True
            log.info("test case pass")
        else:
            log.critical("test case fail")
            assert False

    def test_blank_username_blank_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE test_blank_username_blank_password")
        log.info("Test case started")
        login.input_username('')
        login.input_password('')
        login.click_login()
        time.sleep(3)
        if 'Required' in login.invalid_required():
            assert True
            log.info("Test case pass")
        else:
            log.critical("test case fail")
            assert False
