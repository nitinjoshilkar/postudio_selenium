from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from decouple import config
import logging
import time
import pyautogui

logging.basicConfig(level=logging.DEBUG,
                    filename="postudio.log", 
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filemode='a+') 
console = logging.StreamHandler()
console.setLevel(logging.INFO)
#console.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger_login= logging.getLogger('login.py')
logger_logout= logging.getLogger('logout.py')



def signin():
	try:
		URL_PATH = config('URL')
		driver= webdriver.Chrome()
		driver.implicitly_wait(5)
		driver.set_window_size(1524, 1024)
		#driver.maximize_window()
		actions = ActionChains(driver)
		driver.get(URL_PATH)
		logger_login.info("Connection created successfully")
		time.sleep(1)
		username = driver.find_element_by_xpath('//*[@id="email"]')
		username.clear()
		username.send_keys(config('username'))
		password = driver.find_element_by_xpath('//*[@id="password"]')
		password.clear()
		password.send_keys(config('password'))
		login= driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/form/div[3]/button')
		login.click()
		time.sleep(2)
		logger_login.info("login successfully")
		time.sleep(2)

		''' logout view '''
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div/div/button/span[1]/div').click()
		asset_over= driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]')
		hover = ActionChains(driver).move_to_element(asset_over)
		hover.perform()
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li')
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Sign Out']"))).click()
		time.sleep(2)
		logger_login.info('logout successfully')

		''' close browser '''
		driver.close()
		driver.quit()
	except Exception as e:
		logger_login.debug("Failed to connect internet: %s" %e)
		print("Failed to connect internet: %s" %e)
		driver.close()
		driver.quit()

if __name__ == '__main__':
	count=1
	for checkloop in range(1,50):
		signin()
		count+=1
		logger_login.info('count={}'.format(count))
