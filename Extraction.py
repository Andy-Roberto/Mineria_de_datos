from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

services = Service('./chromedriver.exe')
options = webdriver.ChromeOptions(
)
# options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')
options.add_experimental_option('detach',True)
driver_path = 'C:\\Users\\Andy\\Documents\\Python\\chromedriver.exe'

driver = webdriver.Chrome(service=services,options=options)

driver.get('https://www.kaggle.com/datasets/adityaramachandran27/nasa-near-earth-objects-information')
flag =driver.find_elements(By.XPATH,'/html/body/main/div[1]/div/div[6]')
driver.execute_script("arguments[0].scrollBy(0,200)",flag)
time.sleep(5)
driver.close()