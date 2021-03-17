from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "/Applications/chromedriver"
driver =  webdriver.Chrome(path)

driver.get("https://techwithtim.net")

