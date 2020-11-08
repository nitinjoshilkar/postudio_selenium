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
#import pyautogui
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

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
import pytest

def test_signin():
	try:
		URL_PATH = config('URL')
		driver= webdriver.Chrome(chrome_options=chrome_options)
		#driver= webdriver.Chrome()
		driver.implicitly_wait(5)
		driver.set_window_size(1524, 1024)
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
		login= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/form/div[3]/button')
		login.click()
		time.sleep(2)
		logger_login.info("login successfully")
		time.sleep(2)

		''' create storyboard '''
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[1]/div/div[1]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create Storyboard']"))).click()
		create_storyboard = driver.find_element_by_xpath('//*[@id="createStoryboard"]')
		create_storyboard.clear()
		create_storyboard.send_keys(config('STORYBOARD_NAME_CREATE'))
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[1]/div/div[2]/div[2]/button').click()
		time.sleep(2)
		logger_login.info("storyborad created successfully")
		
		'''back button'''
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button').click()
		time.sleep(3)
		
		''' open storyboard '''
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[2]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Selenium Test2']"))).click()
		logger_login.info("first storyborad opened successfully")
		time.sleep(3)

		''' add storyboard brief '''
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[1]/div/div[1]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[1]/div/div[2]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Add Storyboard Brief']"))).click()
		time.sleep(1)
		storyboard_brief = driver.find_element_by_xpath('//*[@id="brief"]')
		storyboard_brief.clear()
		storyboard_brief.send_keys(config('storyboard_brief'))
		storyboard_update= driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		storyboard_update.click()
		time.sleep(1)
		storyboard_brief_sidemenu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button')
		storyboard_brief_sidemenu.click()
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]')
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[1]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add Storyboard Brief']"))).click()
		time.sleep(1)
		storyboard_brief = driver.find_element_by_xpath('//*[@id="brief"]')
		storyboard_brief.clear()
		storyboard_brief.send_keys(config('storyboard_brief'))
		storyboard_update= driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		storyboard_update.click()
		time.sleep(4)
		logger_login.info("storyboard brief added successfully")

		'''back button'''
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button').click()
		time.sleep(3)
		
		''' open storyboard '''
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[2]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Selenium Test1']"))).click()
		logger_login.info("second storyboard opened successfully")
		time.sleep(3)

		''' add collaborator '''
		logger_login.info("collaborator addition process started")
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[1]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[2]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add users to collaborate on this Storyboard']"))).click()
		time.sleep(3)
		add_collaborator = driver.find_element_by_xpath('//*[@id="users"]')
		add_collaborator.clear()
		add_collaborator.send_keys(config('collaborator_email'))
		time.sleep(2)
		add_collaborator.send_keys(Keys.ENTER)
		collaborator_update=driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Update']"))).click()
		logger_login.info("first collaborator selected")
		time.sleep(5)
		collaborator_sidemenu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button')
		collaborator_sidemenu.click()
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[4]')
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[4]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add Collaborators']"))).click()
		time.sleep(1)
		add_collaborator_sidemenu = driver.find_element_by_xpath('//*[@id="users"]')
		add_collaborator_sidemenu.clear()
		add_collaborator_sidemenu.send_keys(config('collaborator_email2'))
		time.sleep(1)
		add_collaborator_sidemenu.send_keys(Keys.ENTER)
		time.sleep(1)
		collaborator_update=driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		collaborator_update.click()
		time.sleep(4)
		logger_login.info("second collaborator selected")
		
		''' create task '''
		driver.maximize_window()
		logger_login.info("Create task started")
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[2]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[2]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Create & Assign Tasks to your team']"))).click()
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/div/div/div').click()
		driver.find_element_by_xpath('//*[@id="menu-"]/div[3]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Video Editing']"))).click()
		time.sleep(1)
		logger_login.info("Video editing task seleted")
		assign_to = driver.find_element_by_xpath('//*[@id="assignTo"]')
		assign_to.clear()
		assign_to.send_keys(config('assign_task_user'))
		time.sleep(2)
		assign_to.send_keys(Keys.ENTER)
		logger_login.info("Assign task to user selected")
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div/div[3]/div/div/div/button').click()
		time.sleep(2)
		add_date=driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div/div[3]/div/div/div/button')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='26']"))).click()
		logger_login.info("Date selected")
		time.sleep(2)
		description = driver.find_element_by_xpath('//*[@id="description"]')
		description.clear()
		description.send_keys(config('task_description'))
		time.sleep(2)
		create_task = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		create_task.click()
		logger_login.info("Task created successfully")
		time.sleep(4)
		
		''' task details '''
		logger_login.info("Task deletion process started")
		taskdetails_sidemenu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button')
		taskdetails_sidemenu.click()
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[3]')
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[3]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Task Details']"))).click()
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div').click()
		driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Update']"))).click()
		driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button[1]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Delete']"))).click()
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[3]/button[2]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes']"))).click()
		logger_login.info("Task deleted successfully")		
		time.sleep(4)
		
		'''back button'''
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button').click()
		time.sleep(3)
		
		''' open first storyboard '''
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[2]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Selenium Test2']"))).click()
		logger_login.info("first storyborad opened successfully")
		time.sleep(3)

		''' delete first storyboard '''
		logger_login.info("storyboard deletion process started")
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button').click()
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]')
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[5]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Manage Storyboard']"))).click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button[1]').click()
		driver.find_element_by_xpath('//*[@id="delete-storyboard-yes"]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes']"))).click()
		logger_login.info("storyboard deleted successfully")		
		time.sleep(4)
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
		logger_login.error("Failed to connect internet: %s" %e)
		driver.close()
		driver.quit()

if __name__ == '__main__':
	test_signin()
	#testcase added for demo for pull  
