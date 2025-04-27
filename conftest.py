from datetime import datetime

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--headless")  # Убери, если нужен UI
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
