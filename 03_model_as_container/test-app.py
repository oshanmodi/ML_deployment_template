import requests


# In[2]:


# In[3]:


passenger1 = {
    "Pclass": 3,
    "Sex": "male",
    "Age": 34.5,
    "SibSp": 0,
    "Parch": 2,
    "Fare": 7.8292,
    "Cabin": "no",
    "Embarked": "S",
}


# In[4]:


passenger2 = {
    "PassengerId": 2,
    "Survived": 1,
    "Pclass": 1,
    "Name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
    "Sex": "female",
    "Age": 38.0,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": "PC 17599",
    "Fare": 71.2833,
    "Cabin": "C85",
    "Embarked": "C",
}


# In[5]:


# passenger = dftest.iloc[0].to_dict()
url = "http://0.0.0.0:9696/predict"


# In[7]:


requests.get(url)


# In[8]:


response = requests.post(url, json=passenger1)
response.json()


# In[9]:


response = requests.post(url, json=passenger2)
response.json()


# In[ ]:
