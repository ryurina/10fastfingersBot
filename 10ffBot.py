# DON'T CHEAT WITH THIS SCRIPT
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="chromedriver.exe") # Paths to chromedriver
browser.implicitly_wait(5)

def login():
	comp = "https://10fastfingers.com/typing-test/english"
	browser.get(comp)

def typing():
	# Type text
	sleep(5)
	for i in range(1, 189):
		l = browser.find_element_by_xpath('//*[@id="row1"]/span[{}]'.format(i)).text
		browser.find_element_by_xpath('//*[@id="inputfield"]').send_keys(l)
		browser.find_element_by_xpath('//*[@id="inputfield"]').send_keys(Keys.SPACE)

