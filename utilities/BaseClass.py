import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # this will give you the name from which this method being called
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(r'C:\Users\HP\PycharmProjects\PythonSelfFramework\utilities\logfile.log',
                                          mode='a')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s  %(message)s")
        fileHandler.setFormatter(formatter)
        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
