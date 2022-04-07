from selenium import webdriver
import sys
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import tkinter as tk
warnings.filterwarnings("ignore", category=DeprecationWarning)


options = webdriver.ChromeOptions()
options.binary_location = '/snap/bin/brave'
options.add_argument("--remote-debugging-port=9222") 
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("disable-infobars")
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options,executable_path='res/chromedriver')

driver.minimize_window()
# driver.fullscreen_window()

driver.get(sys.argv[1])

driver.implicitly_wait(3)
# try:
#     driver.find_element_by_class_name('mb-text').click()
#     driver.switch_to.window(driver.window_handles[-1])
# except:
#     pass
# element = driver.find_element_by_class_name("bg-blue-500")
# element.c
element = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "bg-blue-500")))
# print(element)
ele=element[0].find_elements_by_tag_name('a') # 

# soup=BeautifulSoup(element[0].get_attribute('innerHTML'), 'html.parser')
# driver.execute_script("arguments[0].click();", element)
# print(ele)#,soup)
ele[0].click()
print('click')
driver.implicitly_wait(20)

element = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "verify_button2")))
# print(element)
re=element[0].click()
print('click')
# print('/'*20,re)
element = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "verify_button")))
# print(element)
element[0].click()
print('click')
time.sleep(10)
element = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "two_steps_btn")))
# print(element[0].get_attribute("href"))#.click()
driver.get(element[0].get_attribute("href"))
print('click')
time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])
element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "btn")))
element[2].click()

element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "btn-success")))
# print(driver.current_url,len(element))
element[0].click()

driver.switch_to.window(driver.window_handles[-1])

element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "btn-primary")))
# print(driver.current_url,len(element))
element[0].click()

driver.switch_to.window(driver.window_handles[-1])

element = WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "btn")))
# element=driver.find_element_by_class_name('mb-4')
# print(driver.current_url,len(element))
element[0].click()

root = tk.Tk()
link=root.clipboard_get()

with open('res/oneL.txt','w') as f:
    f.write(link)

print('DONE '*10)
for i in driver.window_handles:
    driver.switch_to.window(i)
    driver.close()
  
driver.quit()
print('third DONE')