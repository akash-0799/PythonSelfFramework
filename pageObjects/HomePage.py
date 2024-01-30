from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")  # self.driver.find_element(By.LINK_TEXT, "Shop").click()
    name = (By.XPATH, "//div/input[@name= 'name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    radiobutton = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@type= 'submit']")
    message = (By.CLASS_NAME, "alert-success")
    clear = (By.XPATH, "(//input[@type= 'text'])[3]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def checkRadiobutton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)

    def clearForm(self):
        return self.driver.find_element(*HomePage.clear)
