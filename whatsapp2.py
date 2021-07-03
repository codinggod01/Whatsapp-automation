from selenium import webdriver 
import pickle
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
def getname(driver,contact):
# Replace below path with the absolute path 
# to chromedriver in your computer 
    

    # Replace the below string with your own message 

    xp='//*[@id="side"]/div[1]/div/label/div/div[2]'
    search = driver.find_element_by_xpath(xp)
    time.sleep(1)
    search.click()
    time.sleep(1)
    search.send_keys(contact)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(7)
    xp = '//*[@id="main"]/header/div[2]/div[2]/span'



    # In[2]:


    name = driver.find_element_by_xpath(xp).text
    

    # In[4]:


    x = list(name.split(", "))


    # In[5]:





    # In[6]:


    l = len(x)


    # In[7]:


    for i in range(l):
        x[i] = '@' + x[i]



    # In[8]:


    x


    # In[11]:


    xp = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    search = driver.find_element_by_xpath(xp)
    time.sleep(1)
    search.click()


    # In[12]:


    x.pop()
    return x

    
if __name__ == "__main__":
    getname()
    
