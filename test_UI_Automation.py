from selenium import webdriver
from time import *
import pytest



@pytest.fixture(scope="class")
def driver_obj():
    driver=webdriver.Chrome()
    return driver
    #yield
    #driver.quit()

@pytest.mark.usefixtures("driver_obj")
class Test_mysuite:
    def test_case1(self,driver_obj):                                    #Test case to invoke browser.
        driver_obj.get("http://www.rahulshettyacademy.com")
        driver_obj.maximize_window()
        sleep(2)
        #self.quit()
    @pytest.mark.skip
    def test_case2(self,driver_obj):
        assert driver_obj.title=="Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy"

    def test_caseX(self,driver_obj):
        driver_obj.quit()













