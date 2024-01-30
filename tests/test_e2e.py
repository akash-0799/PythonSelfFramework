import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# For optimizing the page object page model integration point must be known so that we can link two POM
# We can skip multiple object creation for different Page Object Model


class TestOne(BaseClass):  # Class name should be start with  Test keyword in the beginning
    def test_e2e(self):
        self.driver.implicitly_wait(4)
        log = self.getLogger()

        homepage = HomePage(self.driver)  # using POM class to initiate driver object

        checkOutPage = homepage.shopItems()

        self.driver.execute_script("window.scrollTo(0,500);")
        time.sleep(2)
        log.info("Getting all the mobile details")
        # self.driver.find_element(By.XPATH, "//a[contains(.,'Shop')]").click()
        AllProducts = checkOutPage.getCardTitles()
        # AllProducts = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in AllProducts:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            log.info(product_name)
            if product_name == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkOutPage.checkOutButton1().click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirmPage = checkOutPage.checkOutButton2()
        log.info("Enter country name as Ind")
        # self.driver.find_element(By.ID, "country").send_keys("Ind")
        confirmPage.countryName().send_keys("Ind")
        self.verifyLinkPresence("India")
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.countrySelect().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.countryFinal().click()
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmPage.countrySubmit().click()
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is "+message)
        assert "Success! Thank you!" in message
