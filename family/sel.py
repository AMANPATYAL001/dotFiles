from selenium import webdriver
import sys
import time
import os
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# driver=webdriver.Chrome('Documents/chromedriver')

# driver.get('https://www.calculatorsoup.com/calculators/math/basic.php')

# one=driver.find_element_by_id('display')

# one.send_keys('230-90')
# driver.find_element_by_name('calculate').click()

# print(one.get_attribute('value'))

# driver.get('https://www.irctc.co.in/nget/train-search')

# driver.find_element_by_class_name('btn-primary').click()
# place=['LUCKNOW NE - LJN','MATHURA JN - MTJ']

# for i,j in zip(driver.find_elements_by_class_name('ui-autocomplete-input'),place): 
#     i.send_keys(j)

# driver.find_element_by_class_name("search_btn").click()


options = webdriver.ChromeOptions()
# os.chdir('/home/amanp')
# options.binary_location = '/home/amanp/snap/brave'
options.add_argument("--remote-debugging-port=9222") 
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("disable-infobars")
# options.add_argument()
# os.chdir('/home/amanp/Documents/family')
driver = webdriver.Chrome(options = options, executable_path='res/chromedriver')

driver.minimize_window()


driver.get(sys.argv[1])

# for i in driver.find_elements_by_class_name('maxbutton-78'):
#     print(i.text,i.get_attribute('href'),end='\n')

# for i in driver.find_elements_by_class_name('has-vivid-red-color')[4:-1]:
#     print(i.text)


wait = WebDriverWait(driver,3)
head=''
c=0
episode_links=''
for i in wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.timed-content-client_show_0_05_0'))):
    # print('aman',i)
    if i.tag_name=='div':
        head=i.text
        # print('patyal',i,head,'end')
        # print(head)
        soup=BeautifulSoup(i.get_attribute('innerHTML'), 'html.parser')
        link=soup.find('a',href=True)['href']
        # soup=BeautifulSoup(soup, 'html.parser')
        for j in soup.find_all('a'):
            c+=1
            episode_links=episode_links+j['href']+' \n'

    # if i.tag_name=='p':
    #     # print(link)
    #     quality=soup.find('span').text
        # print()
        # print(i.get_attribute('innerHTML'))

with open('res/episodeL.txt','w') as f:
    f.write(episode_links)
# print(episode_links)
driver.implicitly_wait(10)

print('DONE '*10)
driver.close()
driver.quit()

sys.exit()
driver.get(link)

try:
    driver.find_element_by_class_name('mb-text').click()
    driver.switch_to.window(driver.window_handles[-1])
except:
    pass
    # driver.find_element_by_class_name('maxbutton-3').click()

# driver.switch_to.window(driver.window_handles[-1])

# driver.implicitly_wait(10)

driver.find_element_by_id('generater').click()

# driver.implicitly_wait(15)
time.sleep(10)

# wait = WebDriverWait(driver,15)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#showlink'))).click()
driver.find_element_by_id('showlink').click()


driver.switch_to.window(driver.window_handles[-1])

with open('lastLink.txt','w') as f:
    f.write(driver.current_url)

time.sleep(2)
driver.quit()

sys.exit()
driver.implicitly_wait(2)
driver.find_element_by_class_name('maxbutton-78').click()

print(driver.window_handles,type(driver.window_handles))

driver.switch_to.window(driver.window_handles[-1])
print('Aman',driver.current_url)

driver.find_element_by_class_name('maxbutton-2').click()

driver.switch_to.window(driver.window_handles[-1])

driver.implicitly_wait(10)

driver.find_element_by_id('generater').click()

driver.implicitly_wait(10)

driver.find_element_by_id('showlink').click()

driver.switch_to.window(driver.window_handles[-1])

print(driver.current_url)