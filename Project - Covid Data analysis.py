#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


covid_df=pd.read_csv(r"C:\Users\heman\Downloads\covid_19_india.csv")
covid_df.head(50)


# In[3]:


covid_df=pd.read_csv(r"C:\Users\heman\Downloads\covid_19_india.csv")
covid_df.tail(50)


# In[4]:


covid_df.isnull().sum()


# In[5]:


covid_df.info()


# In[6]:


covid_df.describe()


# In[7]:


vacine_df=pd.read_csv(r"C:\Users\heman\Downloads\covid_vaccine_statewise.csv")
vacine_df.head()


# In[8]:


vacine_df.tail()


# In[8]:


vacine_df.isnull().sum()


# In[9]:


covid_df.drop(['Sno','ConfirmedIndianNational','ConfirmedForeignNational'],inplace=True,axis=1)
covid_df.head()


# In[10]:


covid_df.Date=pd.to_datetime(covid_df["Date"],format="%Y-%m-%d")
covid_df.head()


# In[11]:


covid_df["Active_cases"]=covid_df["Confirmed"]-(covid_df["Cured"]-covid_df["Deaths"])
covid_df.tail()


# In[12]:


statewise= pd.pivot_table(covid_df,values=["Cured","Deaths","Confirmed"],aggfunc=max,index="State/UnionTerritory")


# In[13]:


statewise["Recovery rate"]= statewise["Cured"]*100/statewise["Confirmed"]


# In[14]:


statewise["Mortality"]= statewise["Deaths"]*100/statewise["Confirmed"]


# In[15]:


statewise=statewise.sort_values(by= "Confirmed",ascending=False)
statewise


# In[16]:


statewise.style.background_gradient(cmap="cubehelix")


# In[17]:


top_10_active_cases=covid_df.groupby(by="State/UnionTerritory").max()[['Active_cases']].sort_values(by=['Active_cases'],ascending=False).reset_index()


# In[18]:


fig=plt.figure(figsize=(16,9))


# In[19]:


plt.title("Top ten states with most active cases ",size =25)


# In[20]:


ax=sns.barplot(data=top_10_active_cases.iloc[:10] , y="Active_cases", x="State/UnionTerritory", linewidth=2, edgecolor="black")


# In[21]:


fig=plt.figure(figsize=(16,9))
plt.title("Top ten states with most active cases ",size =25)

ax=sns.barplot(data=top_10_active_cases.iloc[:10] , y="Active_cases", x="State/UnionTerritory", linewidth=2, edgecolor="black")
plt.xlabel("States/UT")
plt.ylabel("Active Cases")
plt.show()


# In[22]:


#Top states with highest no of deaths

fig=plt.figure(figsize=(18,5))

top_10_deaths=covid_df.groupby(by="State/UnionTerritory").max()[['Deaths']].sort_values(by=['Deaths'],ascending=False).reset_index()


plt.title("States/UT with most deaths",size=25)

ax=sns.barplot(data=top_10_deaths.iloc[:12] , y="Deaths", x="State/UnionTerritory", linewidth=2, edgecolor="black")
plt.xlabel("State/UT")
plt.ylabel("Total no of deaths")


# In[23]:


# growth trend

fig = plt.figure(figsize=(16,9))

ax=sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu'])] ,x='Date',y='Deaths',hue='State/UnionTerritory')

fig=plt.figure(figsize=(16,9))


# In[24]:


fig = plt.figure(figsize=(16,9))

ax=sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu'])] ,x='Date',y='Active_cases',hue='State/UnionTerritory')




# In[25]:


fig=plt.figure(figsize=(16,9))
ax=sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu'])] ,x='Date',y='Active_cases',hue='State/UnionTerritory')


# In[26]:


vacine_df.head()


# In[27]:


vacine_df.info()


# In[28]:


vacine_df.isnull().sum()


# In[29]:


vaccination=vacine_df.drop(columns=["Sputnik V (Doses Administered)","AEFI","18-44 Years (Doses Administered)","45-60 Years (Doses Administered)","60+ Years (Doses Administered)"],axis=1)


# In[30]:


vaccination.head()


# In[31]:


# male vs female vaccination

male=vaccination["Male(Individuals Vaccinated)"].sum()
female=vaccination["Female(Individuals Vaccinated)"].sum()

px.pie(names=(["Male","Female"]),values=[male,female],title="Male and Female Vaccination")


# In[32]:


#Remove rows where state is India

vaccine=vaccination[vaccination["State"]!="India"]


# In[33]:


vaccine["State"].unique()


# In[34]:


vaccine.rename( columns = {"Total Individuals Vaccinated" : "Total"}, inplace = True)
vaccine.head()


# In[ ]:





# In[35]:


# states with maximum vaccinations

max_vac=vaccine.groupby(by="State").sum()[["Total"]].sort_values(by=["Total"],ascending=False).reset_index()
max_vac.head()


# In[36]:


fig=plt.figure(figsize=(16,9))
plt.title("Top 5 states with most vaccinations",size =25)

ax=sns.barplot(data=max_vac.iloc[:5] , y="Total", x="State", linewidth=2, edgecolor="black")
plt.xlabel("States/UT")
plt.ylabel("Total Vaccinated")
plt.show()


# In[37]:


min_vac=vaccine.groupby(by="State").sum()[["Total"]].sort_values(by=["Total"],ascending=True).reset_index()
min_vac.head()


# In[38]:


fig=plt.figure(figsize=(16,9))
plt.title("Top 5 states with most Vaccinations ",size =25)

ax=sns.barplot(data=min_vac.iloc[:5] , y="Total", x="State", linewidth=2, edgecolor="black")
plt.xlabel("States/UT")
plt.ylabel("Total Vaccinated")
plt.show()


# In[ ]:




