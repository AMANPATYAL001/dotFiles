from selenium import webdriver
import sys
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

options = webdriver.ChromeOptions()
options.binary_location = '/snap/bin/brave'
options.add_argument("--remote-debugging-port=9222") 
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("disable-infobars")
driver = webdriver.Chrome(options=options,executable_path='Documents/chromedriver')

driver.minimize_window()

driver.get(sys.argv[1]) 

driver.implicitly_wait(10)


if driver.title=='GPLOAD':
    print('GPLOAD')
    # soup=BeautifulSoup(driver.find_element_by_class_name('col-md-4').get_attribute('innerHTML'), 'html.parser')
    driver.find_element_by_class_name('btn-primary').click()
    driver.switch_to.window(driver.window_handles[0])
    # print(soup)
    driver.implicitly_wait(10)
    time.sleep(5)
    var=driver.find_element_by_class_name('btn-primary').get_attribute('href')
    print(var)
    
    with open('gploadL.txt','w') as f:
       f.write(var)
else:
    print('Sorry unknown ERRRRROR,  contact AmanP')
