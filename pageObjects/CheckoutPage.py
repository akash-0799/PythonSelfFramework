from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    itemTitles = (By.XPATH,
                  "//div[@class='card h-100']")  # for -->> self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    checkoutButtonPrimary = (By.CSS_SELECTOR,
                             "a[class*='btn-primary']")  # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkoutButtonSecond = (By.XPATH,
                            "//button[@class='btn btn-success']")  # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.itemTitles)

    def checkOutButton1(self):
        return self.driver.find_element(*CheckoutPage.checkoutButtonPrimary)

    def checkOutButton2(self):
        self.driver.find_element(*CheckoutPage.checkoutButtonSecond).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
