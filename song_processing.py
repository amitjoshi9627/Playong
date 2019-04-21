from utils import *
from account_processing import *
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import getpass 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def song_interrupt_check(browser,song_time):
	timer  = browser.find_element_by_xpath('//*[@id="track-elapsed"]').text
	track_time = to_seconds(timer)

	if track_time < song_time:
		time.sleep(song_time - track_time)
	while track_time < song_time :
		timer  = browser.find_element_by_xpath('//*[@id="track-elapsed"]').text
		track_time = to_seconds(timer)

		if track_time < song_time:
			time.sleep(song_time - track_time)

def more_than_1_song_play(browser,num_songs = 2):
	song_number = 2
	while(song_number<=num_songs):
		try:
			browser.find_elements_by_xpath('//*[@id="fwd"]')[0].click()
			time.sleep(1)
			track_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/strong/a').text
			album_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/span/a').text
			timer = browser.find_element_by_xpath('//*[@id="track-time"]').text
			song_time = to_seconds(timer)	
			print(f'{song_number}.Playing Song "{track_name}" from the album "{album_name}"...\n')
			show_notificaton(track_name, album_name)
			time.sleep(song_time-2)

			song_interrupt_check(browser,song_time)
			song_number+=1
		except:
			try:
				close_popup_ad(browser)
			except:
				close_login_box(browser)

def play_user_timed_songs(browser,song_time = 20,num_songs = 25):
	browser.find_elements_by_xpath('/html/body/div[8]/div/section/div/div[2]/div[2]/div/div/button')[0].click()
	time.sleep(1)
	track_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/strong/a').text
	album_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/span/a').text
	print(f'\n{1}.Playing Song "{track_name}" from the album "{album_name}"...\n')
	show_notificaton(track_name, album_name)
	time.sleep(song_time)
	song_interrupt_check(browser,song_time)
	song_number = 2
	while(song_number<=num_songs):
		try:
			browser.find_elements_by_xpath('//*[@id="fwd"]')[0].click()
			time.sleep(1)
			track_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/strong/a').text
			album_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/span/a').text
			print(f'{song_number}.Playing Song "{track_name}" from the album "{album_name}"...\n')
			show_notificaton(track_name, album_name)
			time.sleep(song_time)
			song_interrupt_check(browser,song_time)
			song_number+=1
		except:
			try:
				close_popup_ad(browser)
			except:
				close_login_box(browser)

	browser.find_element_by_xpath('//*[@id="pause"]').click()

def play_default_timed_songs(browser,num_songs):
	try:
		browser.find_elements_by_xpath('/html/body/div[8]/div/section/div/div[2]/div[2]/div/div/button')[0].click()
		time.sleep(1)
		timer = browser.find_element_by_xpath('//*[@id="track-time"]').text
		song_time = to_seconds(timer)
		track_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/strong/a').text
		album_name = browser.find_element_by_xpath('/html/body/article/div/div[3]/section/div[3]/div/span/a').text
		show_notificaton(track_name, album_name)
		print(f'\n{1}.Playing Song "{track_name}" from the album "{album_name}"...\n')
		time.sleep(song_time-2)
		song_interrupt_check(browser,song_time)
		if num_songs >1:
			more_than_1_song_play(browser,num_songs)

	except:
		try:
			close_popup_ad(browser)
		except:
			close_login_box(browser)
		if num_songs >1:
			more_than_1_song_play(browser,num_songs)
	browser.find_element_by_xpath('//*[@id="pause"]').click()
