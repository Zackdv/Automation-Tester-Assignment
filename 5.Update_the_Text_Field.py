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

slider_input = driver.find_element(By.XPATH,"//h4[@class='MuiTypography-root MuiTypography-h4 crimsonPro css-12siehf']")

slider_element = driver.execute_script("arguments[0].scrollIntoView();",slider_input)

mini = driver.find_element(By.XPATH,"//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-sy3s50']")

action = ActionChains(driver)

yes = action.drag_and_drop_by_offset(mini,94,0).perform()  # 820


step_5 = action.drag_and_drop_by_offset(mini,-39,0).perform() #560