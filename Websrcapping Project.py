#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page = requests.get('https://www.imdb.com/chart/top')
page


# In[8]:


soup = BeautifulSoup(page.content)


# In[9]:


soup


# In[10]:


scraped_movies = soup.find_all('td',class_="titleColumn")
scraped_movies


# In[16]:


movies = []
for movie in scraped_movies:
    movie = movie.get_text().replace('\n', '')
    movie = movie.strip(" ")
    movies.append(movie)
movies


# In[17]:


scraped_ratings = soup.find_all('td',class_="ratingColumn imdbRating")
scraped_ratings


# In[18]:


ratings = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n','')
    ratings.append(rating)
ratings


# In[19]:


data = pd.DataFrame()
data['Movie names'] = movies
data['Ratings'] = ratings
data.head(100)


# Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)?

# In[20]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[21]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[22]:


soup = BeautifulSoup(page.content)
soup


# In[24]:


scraped_names = soup.find_all('div',class_="presidentListing")
scraped_names


# In[28]:


names = []
for name in scraped_names:
    name = name.get_text().replace('\n','')
    names.append(name)
names


# In[33]:


data = pd.DataFrame()
data['Names'] = names
data.head(14)


# Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape?

# In[37]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# In[38]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[44]:


soup = BeautifulSoup(page.content)
soup


# In[63]:


scraped_teams = soup.find_all('span', class_="u-hide-phablet")
scraped_teams


# In[64]:


teams = []
for team in scraped_teams:
    team = team.get_text()
    teams.append(team)
teams


# In[65]:


data = pd.DataFrame()
data ['Teams'] = teams
data.head(10)


# In[69]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
soup = BeautifulSoup(page.content)
soup


# In[70]:


scraped_players = soup.find_all('div',class_="rankings-block__banner--player-info")
scraped_players


#  Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world?
# 

# In[74]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[77]:


page = requests.get('https://www.cnbc.com/world/?region=world')
page


# In[78]:


soup = BeautifulSoup(page.content)
soup


# In[79]:


scraped_headlines = soup.find_all('div',class_='LatestNews-container')
scraped_headlines


# In[80]:


headlines=[]
for headline in scraped_headlines:
    headline = headline.get_text()
    headlines.append(headline)
headlines


# Write a python program to scrape the details of most downloaded articles from AI in last 90 days?

# In[82]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[83]:


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[86]:


soup = BeautifulSoup(page.content)
soup


# In[90]:


scraped_titles = soup.find_all('li',class_="sc-9zxyh7-1 sc-9zxyh7-2 exAXfr jQmQZp")
scraped_titles


# In[91]:


titles = []
for title in scraped_titles:
    title = title.get_text()
    titles.append(title)
titles


# In[92]:


data = pd.DataFrame()
data ['Titles'] = titles
data.head(25)


# Write a python program to scrape mentioned details from dineout.co.in?

# In[93]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[94]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[95]:


soup = BeautifulSoup(page.content)
soup


# In[97]:


titles=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    titles.append(i.text)
    
titles


# In[99]:


df=pd.DataFrame({'Restaurent Name':titles})
df


# In[100]:


location = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[101]:


df=pd.DataFrame({'Location':location})
df


# In[106]:


price = []
for i in soup.find_all('span',class_="double-line-ellipsis"):
     price.append(i.text)
price


# In[107]:


images = []
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
images


# In[108]:


df=pd.DataFrame({'Images URL':images})
df


# In[109]:


df=pd.DataFrame({'Restaurent Name':titles,'Location':location,'Price':price,'Images URL':images,})
df


#  Write a python program to scrape the details of top publications from Google Scholar.

# In[111]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[112]:


page = requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[113]:


soup = BeautifulSoup(page.content)
soup


# In[114]:


rank=[]
for i in soup.find_all('td',class_="gsc_mvt_t"):
    rank.append(i.text)
    
rank


# In[115]:


df=pd.DataFrame({'Rank':rank})
df


# In[116]:


h5_index = []
for i in soup.find_all('td',class_="gsc_mvt_n"):
    h5_index.append(i.text)
    
h5_index
    


# In[123]:


df=pd.DataFrame({'h5 Index':h5_index})
df
data.head(100)


# In[ ]:





# In[119]:


h5_median = []
for i in soup.find_all('span',class_="gs_ibl gsc_mp_anchor"):
    h5_median.append(i.text)
    
h5_median


# In[120]:


df=pd.DataFrame({'h5 Median':h5_median})
df


# Write a python program to display all the header tags?

# In[129]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[131]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[132]:


soup = BeautifulSoup(page.content)
soup


# In[133]:


tags = []
for i in soup.find_all('span',class_="mw-headline"):
    tags.append(i.text)
    
tags


# In[134]:


df = pd.DataFrame({'Tags':tags})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




