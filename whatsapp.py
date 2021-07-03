from selenium import webdriver 
import pickle
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from whatsapp2 import getname

# Replace below path with the absolute path 
# to chromedriver in your computer 
options = webdriver.ChromeOptions();
options.add_argument("user-data-dir=~/.chrome_driver_session")
# Create the folder. Change path accordingly


driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")

time.sleep(20)

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
contact = input("Group or person name:")
names = []
if input("is it a group:")== "yes":
	names = getname(driver,contact)
# Replace the below string with your own message 
s = input("Message:")
xp='//*[@id="side"]/div[1]/div/label/div/div[2]'
search = driver.find_element_by_xpath(xp)
time.sleep(1)
search.click()
time.sleep(1)
search.send_keys(contact)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)

xp = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
search = driver.find_element_by_xpath(xp)
search.click()
n = int(input("No. of times'"))
for i in range(n):
	search.send_keys(s)

	search.send_keys(Keys.RETURN)


driver.close()		

