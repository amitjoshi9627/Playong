# import notify2
import os
import subprocess
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import getpass
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def complete_captcha(browser):
    try:
        browser.find_element_by_xpath(
            '//*[@id="recaptcha-anchor"]/div[1]').click()
    except:
        return


def accept_cookies(browser):
    try:
        browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/a').click()  # Accepting Cookies
    except:
        return


def close_promo_ad(browser):
    try:
        browser.find_element_by_xpath('//*[@id="vid-promo-close"]').click()
    except:
        return


def close_login_box(browser):
    try:
        browser.find_element_by_xpath('//*[@id="panel-close"]').click()
    except:
        return


def show_notificaton(first_message, last_message, play=1):
    if play:
        track_name = first_message.replace(' ', '_')
        album_name = last_message.replace(' ', '_')
        message = f"{track_name}"
        if os.name == 'posix':
            title = "Playong"
            subprocess.call(['notify-send', title, message])
        else:
            print(message)
    else:
        message = f"{first_message} {last_message}! for using the Program!!"
        if os.name == 'posix':
            title = "Playong"
            subprocess.call(['notify-send', title, message])
        else:
            print(message)


def to_seconds(timer):
    minutes = int(timer.split(':')[0])
    sec = int(timer.split(':')[1])
    return minutes*60+sec


def close_popup_ad(browser):
    browser.find_element_by_xpath('//*[@id="idle-unit-dismiss"]').click()
