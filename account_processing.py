from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import getpass 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils import *

def login_user(browser,email='',password=''):
	print('Redirecting to login page..')
	browser.find_element_by_xpath('//*[@id="login-btn"]').click()
	if email is '':
		email,password = take_credentials()
	browser.find_element_by_id("login_username").send_keys(email)
	browser.find_element_by_id("login_password").send_keys(password)
	browser.find_element_by_xpath('//*[@id="static-login-btn"]').click()

def logout_user(browser):
	print("\nThank you for your using the program! Logging you out from jiosaavn...")
	show_notificaton("Thank","You",0)
	action = ActionChains(browser)
	menu = browser.find_element_by_class_name('user-name')
	action.move_to_element(menu).perform()
	menu.click()
	browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[3]/ol/li[4]/a').click()
	time.sleep(2)
	print('Logout..successful...')	

def check_credentials(browser):
	print('Checking credentials...Please wait..')
	time.sleep(5)
	try:
		close_promo_ad(browser)
		accept_cookies(browser)
		success = True
	except:
		success = False
	return success

def wrong_credentials_check(browser,counts =1):
	while success!=True:
		print("\nWrong username/password entered.Please try again...\n")
		email = input("Enter your email for jiosaavn account: ")
		password = getpass.getpass(f"Enter password for {email}: ")

		email_element = browser.find_element_by_id("login_username")
		email_element.clear()
		email_element.send_keys(email)

		pswd_element = browser.find_element_by_id("login_password")
		pswd_element.clear()
		pswd_element.send_keys(password)

		browser.find_element_by_xpath('//*[@id="static-login-btn"]').click()
		success = check_credentials(browser)
		counts+=1
		if counts > 4:
			print('Too many unsuccessful attempts done. Exiting...\n')
			break
	return counts

def go_without_login(browser):
	return False

def take_credentials():
	email = input("Enter your email for jiosaavn account: ")
	password = getpass.getpass(f"Enter password for {email}: ")
	return email,password

def prompt(browser):
	response = int(input("Press 1 to Log in with you account else Press 0: "))
	if response:
		login_user(browser)
		return True
	else:
		go_without_login(browser)
