#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the Libraries
import requests
import json
import pandas as pd


# In[2]:


# Bitcon price index.
# Create a requests variables
bitcoin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# Print the status_code.
print(bitcoin.status_code)

# Print the JSON response
print(bitcoin.json())


# In[3]:


# Retrieve the headers
bitcoin.headers


# In[4]:


# Parse JSON data with loads()
bitcoin_content = json.loads(bitcoin.text)

# View the content.
print(type(bitcoin_content))
bitcoin_content


# In[5]:


print(bitcoin_content)


# In[6]:


# Formatting json 
print(json.dumps(bitcoin_content, indent=4))


# In[7]:


# Create a Dataframe directly from the output.
bitcoin_df = pd.DataFrame(bitcoin_content)

# View the DataFrame
bitcoin_df.head


# In[9]:


# Save the JSON file to .json
# Create the JSON file.
bitcoin_json = json.dumps(bitcoin_content)

with open ('bitcoin_json.json', 'w') as f:
    json.dump(bitcoin_content, f)
    
# Save as a CSV file without index
bitcoin_df.to_csv('bitcoin_csv.csv', index=False)


# In[10]:


# USA population data.
import requests
import json
import pandas as pd


# In[11]:


# Create a request variable.
pop = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

# Print the status_code.
print(pop.status_code)

# Print the JSON response.
print(pop.json())


# In[12]:


# Retrieve headers
pop.headers


# In[14]:


# Parse JSON data with loads()
pop_content = json.loads(pop.text)

# View the content
print(type(pop_content))
print(pop_content)


# In[15]:


# Formatting JSON
print(json.dumps(pop_content, indent=4))


# In[ ]:




