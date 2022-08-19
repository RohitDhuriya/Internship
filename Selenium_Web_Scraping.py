#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[3]:


driver = webdriver.Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[4]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[5]:


driver.get("https://www.naukri.com/")


# In[6]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[7]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[8]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[9]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[10]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)

    
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
    

company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
    

experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]//span')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience) 


# In[11]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[12]:


df=pd.DataFrame({'Job_Title':job_title,'Job_Location':job_location,'Company_name':company_name,'Experience_required':experience_required})
df


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.

# In[13]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[14]:


driver = webdriver.Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[15]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[16]:


driver.get('https://www.naukri.com/')


# In[17]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[18]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore/Bengaluru')


# In[19]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[20]:


job_title=[]
job_location=[]


# In[21]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    


# In[22]:


print(len(job_title),len(job_location))


# In[23]:


df=pd.DataFrame({'Job_Title':job_title,'Job_Location':job_location})
df


# Q3: In this question you have to scrape data using the filters available on the webpage as shown below:

# In[24]:


driver = webdriver.Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[25]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[26]:


driver.get('https://www.naukri.com/')


# In[27]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[28]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
location.send_keys('Delhi')


# In[29]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:

# In[ ]:


driver = webdriver.Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[ ]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[ ]:


driver.get('https://www.flipkart.com/')


# In[ ]:


product=driver.find_element(By.CLASS_NAME,"_3704LK")
product.send_keys('sunglasses')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[ ]:


brands = []
product_discription = []
price = []


# In[ ]:


start=0
end=3
for page in range(start,end):
    brands_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brands_tags:
        brands.append(i.text)
    next_button=driver.find_elements(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[ ]:





# In[ ]:




