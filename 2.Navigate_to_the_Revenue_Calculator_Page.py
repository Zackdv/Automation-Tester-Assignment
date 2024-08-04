
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Service_obj = Service(r"C:\Python\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=Service_obj)

driver.implicitly_wait(15)

driver.get("https://www.fitpeo.com/")

driver.maximize_window()

driver.find_element(By.XPATH,"//div[contains(text(),'Revenue Calculator')]").click()