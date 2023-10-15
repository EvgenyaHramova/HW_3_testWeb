import pytest
import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    #browser = testdata['browser']


@pytest.fixture()
def browser():    
    service = Service(testdata['driver_path'])
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)        
    driver.maximize_window()
    yield driver
    driver.quit()


    