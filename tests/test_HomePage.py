import time

import pytest

from TestData.HomePageData import HomePageData  # Package - Filename - Class-name
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        self.driver.implicitly_wait(4)
        log = self.getLogger()
        homepage = HomePage(self.driver)

        log.info("Name is " + getData["name"])
        homepage.getName().send_keys(getData["name"])

        log.info("Email is " + getData["email"])
        homepage.getEmail().send_keys(getData["email"])

        homepage.getPassword().send_keys(getData["password"])
        homepage.clickCheckbox().click()

        log.info("Gender is " + getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.checkRadiobutton().click()
        homepage.clickSubmit().click()
        message = homepage.getMessage().text
        print(message)
        assert 'Success' in message  # To pass or fail the test based on validation
        time.sleep(2)
        homepage.clearForm().clear()
        time.sleep(2)
        self.driver.refresh()

    # params supports both tuple and dictionary data type but must be wrapped in a list[]

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
