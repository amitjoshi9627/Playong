import notify2
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import getpass 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def accept_cookies(browser):
	try:
		browser.find_element_by_xpath('/html/body/div[4]/div/div/a').click() # Accepting Cookies
	except:
		return
def close_promo_ad(browser):
	try:
		browser.find_element_by_xpath('//*[@id="vid-promo-close"]').click()
	except:
		return


def show_notificaton(first_message,last_message,play = 1):
	if play:
		track_name = first_message
		album_name = last_message
		message =f"Playing Song '{track_name}' from Album '{album_name}'"
		notify2.init('song')
		n = notify2.Notification(message,icon = "media-playback-start")
		n.show()
	else:
		message = f"{first_message} {last_message}! for using the Program!!"
		notify2.init('logout')
		n = notify2.Notification(message,icon = "application-exit")
		n.show()

def to_seconds(timer):
	minutes = int(timer.split(':')[0])
	sec = int(timer.split(':')[1])
	return minutes*60+sec

def close_popup_ad(browser):
	browser.find_element_by_xpath('//*[@id="idle-unit-dismiss"]').click()