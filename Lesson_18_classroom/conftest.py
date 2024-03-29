import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def chrome():
    service = Service(executable_path='C:\\Users\\Podli\\OneDrive\\Рабочий стол\\Hillel\\Hillel_Course_AQA_Podlinnov\\Lesson_18_classroom\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    # driver.close()  # закриває вкладку
    driver.quit()  # закриває браузер
