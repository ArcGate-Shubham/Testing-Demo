import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard_data
from Utilities.logger import logclass


@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_correct_username_correct_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        log.info("TEST CASE, test_correct_username_correct_password")
        log.info("Test case starting")
        lg.input_username('Admin')
        lg.input_password('admin123')
        lg.click_login()
        time.sleep(3)
        if 'Dashboard' in db.dashboard():
            assert True
            log.info("Test case pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_incorrect_username_correct_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("TEST CASE test_incorrect_username_correct_password")
        log.info("Test case started")
        lg.input_username('Amin')
        lg.input_password('admin123')
        lg.click_login()
        time.sleep(3)
        if 'Invalid credentials' in lg.invalid_msg():
            assert True
            log.info("Test case pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_correct_username_incorrect_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("TEST CASE test_correct_username_incorrect_password")
        log.info("Test case started")
        lg.input_username('Admin')
        lg.input_password('admin23')
        lg.click_login()
        time.sleep(3)
        if 'Invalid credentials' in lg.invalid_msg():
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case failed")
            assert False

    def test_incorrect_username_incorrect_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("TEST CASE test_incorrect_username_incorrect_password")
        lg.input_username('admin')
        lg.input_password('admin12')
        lg.click_login()
        time.sleep(3)
        if 'Invalid credentials' in lg.invalid_msg():
            assert True
            log.info("test case pass")
        else:
            log.critical("test case failed")
            assert False

    def test_blank_username_correct_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("TEST CASE test_blank_username_correct_password")
        log.info("Test Case started")
        lg.input_username('')
        lg.input_password('admin123')
        lg.click_login()
        time.sleep(3)
        if 'Required' in lg.invalid_required():
            assert True
            log.info("test case pass")
        else:
            log.critical("test case failed")
            assert False

    def test_correct_username_blank_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("TEST CASE test_correct_username_blank_password")
        lg.input_username('Admin')
        lg.input_password('')
        lg.click_login()
        time.sleep(3)
        if 'Required' in lg.invalid_required():
            assert True
            log.info("test case pass")
        else:
            log.critical("test case fail")
            assert False

    def test_blank_username_blank_password(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("TEST CASE test_blank_username_blank_password")
        log.info("Test case started")
        lg.input_username('')
        lg.input_password('')
        lg.click_login()
        time.sleep(3)
        if 'Required' in lg.invalid_required():
            assert True
            log.info("Test case pass")
        else:
            log.critical("test case fail")
            assert False
