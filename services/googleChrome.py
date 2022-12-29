from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import time

class ChromeBrowser():

    def __init__(self, ):
        pass

def addChromeUser(user):
    opt = webdriver.ChromeOptions()
    opt.add_argument("--user-data-dir=" + os.getcwd() + "/profile/" + user)
    browser = webdriver.Chrome(options=opt)
    browser.get("chrome://settings/")
    time.sleep(10)
    browser.close

