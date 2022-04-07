from selenium import webdriver
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

options = webdriver.ChromeOptions()
options.binary_location = '/snap/bin/brave'
options.add_argument("--remote-debugging-port=9222") 
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("disable-infobars")
driver = webdriver.Chrome(options=options,executable_path='chromedriver')

driver.minimize_window()

driver.get('https://episodes.mflixblog.xyz/archives/12402#clickimage')

driver.find_element_by_class_name('jeg_search_input').send_keys(sys.argv[1])

driver.find_element_by_class_name('jeg_search_button').click()


wait = WebDriverWait(driver, 5)
items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.jeg_post_title a')))

title=[]
links=[]
for i in items:
    # print(i.text)
    title.append(i.text)
    links.append(i.get_attribute('href'))
    # print(i.get_attribute('href'),end='\n')

with open('Titles.txt','w') as f:
    for i in title:
        f.write(f'{i}\n')
        
with open('Links.txt','w') as f:
    for i in links:
        f.write(f'{i}\n')

driver.quit()
# print(os.environ['test_var'])
# for i in driver.find_elements_by_class_name('jeg_post_title'):
# print(i.text)
# print(i.get_attribute('href'))

# for i in driver.find_element_by_xpath("//[@class='jeg_post_title']//a"):
# print(i)
