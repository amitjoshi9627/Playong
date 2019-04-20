from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import getpass 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils import *
from account_processing import *
from song_processing import *

try:
	opts = Options()
	opts.set_headless()
	assert opts.headless
	browser = Firefox(options = opts)
	start = time.time()
	print('Starting the program. Please wait...\n')
	browser.get('https://www.jiosaavn.com/')
	end = time.time()
	print(f'Total time to load the page: {round(end - start,5)} seconds.\n')

	accept_cookies(browser)
	close_promo_ad(browser)

	counts = 1

	prompt(browser)
	
	success =check_credentials(browser)

	if not success:
		counts = wrong_credentials_check(browser,counts)

	if counts <=4:
		print('\nLogin successful! Please wait...\n')

		print('Redirecting to the Weekly top-30 songs page...\n')
		browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/section[1]/div[1]/a').click()
		print('Here is your weekly playlist of Hindi top-30 Songs from jiosaavn. Hope you will like it!!..')

		num_songs = int(input('\nHow many songs you want to play? '))
		if num_songs>0:
			timer = input('\nPress Y for to set the duration of songs or Press N to play default duration: ')
			if timer.lower() == 'y':
				song_time = int(input('\nHow long do you want to play each song(seconds)? '))
				play_user_timed_songs(browser,song_time,num_songs)
			else:
				play_default_timed_songs(browser,num_songs)
			
	logout_user(browser)

	browser.close()

except Exception as error:
	
	print('\nWe are really sorry! But due to some technical error the program is exiting. Thank You!')