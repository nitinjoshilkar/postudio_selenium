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

		

		''' create storyboard '''
		#driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[1]/div/div[1]/div')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create Storyboard']"))).click()
		#create_storyboard = driver.find_element_by_xpath('//*[@id="createStoryboard"]')
		#create_storyboard.clear()
		#create_storyboard.send_keys(config('STORYBOARD_NAME'))
		#driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[1]/div/div[2]/div[2]/button').click()
		#time.sleep(4)
		
		'''back button'''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button').click()
		#time.sleep(4)
		

		''' open storyboard '''
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div')
		driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[2]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='50.0 GB Left']"))).click()
		time.sleep(5)

		''' browse assets and folders'''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[4]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[4]/div/div/div')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Browse Assets']"))).click()
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[4]/div[1]/div[1]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Upload Assets']"))).click()
		#pyautogui.moveTo(250, 300, duration = 1)
		#pyautogui.click(250, 300)
		#time.sleep(2)
		#print(pyautogui.position())
		#pyautogui.moveTo(500, 230, duration = 1)
		#pyautogui.click(500, 230)
		#print(pyautogui.position())
		#pyautogui.moveTo(1250, 50, duration = 1)
		#pyautogui.click(1250, 50)
		#time.sleep(8)

		''' add storyboard brief '''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[1]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[1]/div/div[1]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[1]/div/div[2]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add Brief to the Storyboard for your team']"))).click()
		#time.sleep(2)
		#storyboard_brief = driver.find_element_by_xpath('//*[@id="brief"]')
		#storyboard_brief.clear()
		#storyboard_brief.send_keys(config('storyboard_brief'))
		#storyboard_update= driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		#storyboard_update.click()
		#time.sleep(2)
		#storyboard_brief_sidemenu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button')
		#storyboard_brief_sidemenu.click()
		#driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]')
		#driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[1]/div')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add Storyboard Brief']"))).click()
		#time.sleep(1)
		#storyboard_brief = driver.find_element_by_xpath('//*[@id="brief"]')
		#storyboard_brief.clear()
		#storyboard_brief.send_keys(config('storyboard_brief'))
		#storyboard_update= driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		#storyboard_update.click()
		#time.sleep(2)

		''' add collaborator '''
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[1]')
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[2]')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add users to collaborate on this Storyboard']"))).click()
		time.sleep(3)
		add_collaborator = driver.find_element_by_xpath('//*[@id="users"]')
		add_collaborator.clear()
		add_collaborator.send_keys(config('collaborator_email'))
		asset_over= driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/div/div/div/div/button')
		hover = ActionChains(driver).move_to_element(asset_over)
		hover.perform()
		#time.sleep(4)
		pyautogui.moveTo(1200, 380)
		pyautogui.click(1200, 380)
		print(pyautogui.position())
		time.sleep(2)
		collaborator_update=driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		collaborator_update.click()
		time.sleep(4)
		collaborator_sidemenu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button')
		collaborator_sidemenu.click()
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[4]')
		driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[4]/div')
		wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add Collaborators']"))).click()
		time.sleep(1)
		add_collaborator_sidemenu = driver.find_element_by_xpath('//*[@id="users"]')
		add_collaborator_sidemenu.clear()
		add_collaborator_sidemenu.send_keys(config('collaborator_email2'))
		asset_over= driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/div/div/div/div/button')
		hover = ActionChains(driver).move_to_element(asset_over)
		hover.perform()
		#time.sleep(4)
		pyautogui.moveTo(1200, 380)
		pyautogui.click(1200, 380)
		print(pyautogui.position())
		time.sleep(2)
		collaborator_update=driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		collaborator_update.click()
		time.sleep(4)
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[1]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[2]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add users to collaborate on this Storyboard']"))).click()
		#time.sleep(8)

		''' create task '''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[2]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[2]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Create & Assign Tasks to your team']"))).click()
		#time.sleep(3)
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/div/div/div').click()
		#driver.find_element_by_xpath('//*[@id="menu-"]/div[3]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Color Grading']"))).click()
		#time.sleep(3)
		#assign_to = driver.find_element_by_xpath('//*[@id="assignTo"]')
		#assign_to.clear()
		#assign_to.send_keys(config('assign_task_user'))
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[2]/div/div/div').click()
		#time.sleep(4)
		#description = driver.find_element_by_xpath('//*[@id="description"]')
		#description.clear()
		#description.send_keys(config('task_description'))
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[3]/div/div/div/button').click()
		##driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[1]/div[1]')
		##driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div[4]/div[7]/button')
		##wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='25']"))).click()
		## /html/body/div[5]/div[3]/div/div/div[1]/div[1]/button[2]
		#driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[1]/div[1]/button[2]').click()
		## /html/body/div[5]/div[3]/div/div/div[2]/div/div[3]/div[4]/button
		#driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div[3]/div[4]/button')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='12']"))).click()
		#print('date seleted')
		#time.sleep(5)
		#create_task = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button')
		#create_task.click()
		#time.sleep(4)
		
		''' task details '''
		#taskdetails_sidemenu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button')
		#taskdetails_sidemenu.click()
		#time.sleep(3)
		#driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[3]')
		#driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[3]/div')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Task Details']"))).click()
		#time.sleep(3)
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/div').click()
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button').click()
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button[1]').click()
		#asset_over= driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/button[2]')
		#hover = ActionChains(driver).move_to_element(asset_over)
		#hover.perform()
		#driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/button[2]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes']"))).click()
		#time.sleep(4)

		''' back button '''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button').click()
		#time.sleep(4)
		

		''' open storyboard '''
		#driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]')
		#driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/header/div/div')
		#driver.find_element_by_xpath('//*[@id="storyboard_tabs-tabpanel-0"]/div/div/div/div[2]/div')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Selenium Test1']"))).click()
		#time.sleep(5)

		''' delete collaborator '''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[1]')
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[3]/div[3]/div/div[2]')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Add users to collaborate on this Storyboard']"))).click()
		#time.sleep(20)

		''' delete storyboard '''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/button').click()
		#time.sleep(2)
		#driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]')
		#driver.find_element_by_xpath('//*[@id="customized-menu"]/div[3]/ul/li[5]/div')
		#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Manage Storyboard']"))).click()
		#time.sleep(1)
		#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[3]/button[1]').click()
		#time.sleep(1)
		#driver.find_element_by_xpath('/html/body/div[9]/div[3]/div')
		#driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/div[3]')
		#delete_storyboard=driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/button[2]')
		#delete_storyboard.click()
		#time.sleep(6)

		'''back button'''
		#driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button').click()
		#time.sleep(2)
		

		
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
		time.sleep(2)
		

		''' close browser '''
		driver.close()
		driver.quit()
	except Exception as e:
		logger_login.debug("Failed to connect internet: %s" %e)
		print("Failed to connect internet: %s" %e)
		driver.close()
		driver.quit()

if __name__ == '__main__':
    signin()