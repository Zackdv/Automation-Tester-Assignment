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

slider_action_820 = action.drag_and_drop_by_offset(mini,94,0).perform()  # 820

slider_action_560  = action.drag_and_drop_by_offset(mini,-39,0).perform() #560

checkbox_CPT_99091_scroll =  driver.execute_script("window.scrollBy(0,360)","")

CPT_99091_item = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-rfiegf']//div[1]//label[1]//span[1]//input[1]").click()

CPT_99453_item = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-1p19z09']//div[2]//label[1]//span[1]//input[1]").click()

checkbox_next_scroll =  driver.execute_script("window.scrollBy(0,400)","")

CPT_99454_item = driver.find_element(By.XPATH,"//div[3]//label[1]//span[1]//input[1]").click()

further_scroll =  driver.execute_script("window.scrollBy(0,900)","")

CPT_99474_item = driver.find_element(By.XPATH,"//div[8]//label[1]//span[1]//input[1]").click()

expected_reimbursement = "$110295"

actual_reimbursement = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 inter css-hocx5c']"))).text

if actual_reimbursement == expected_reimbursement:
    print(f"Validation passed: {actual_reimbursement}")
else:
    print(f"Validation failed: Expected {expected_reimbursement}, but got {actual_reimbursement}")

driver.quit()












