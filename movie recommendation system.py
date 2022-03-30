#!/usr/bin/env python
# coding: utf-8

# In[242]:


import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")


# In[243]:


warnings.filterwarnings('ignore')


# In[244]:


columns_names=["user_id","movie_id","rating","timestamp"]
dframe=pd.read_csv('movie_data/ml-100k/u.data',sep='\t',names=columns_names)


# In[245]:


dframe.head()


# In[246]:


dframe.shape


# In[247]:


dframe["user_id"].nunique()


# In[248]:


dframe["movie_id"].nunique()


# In[249]:



# dframe=pd.read_csv('movie_data/ml-100k/u.item',sep='\t',header=None)


# In[250]:


file ='movie_data/ml-100k/u.item'


# In[251]:


mframe = pd.read_csv(file,encoding='ISO-8859-1',sep='|')
mframe.head()
mframe.shape


# In[252]:


frame=pd.DataFrame(mframe)


# In[253]:


frame.head()


# In[254]:


frame=frame.iloc[:,:2]


# In[255]:


frame.head()


# In[256]:


frame.columns=["movie_id","title"]


# In[257]:


dframe=pd.merge(dframe,frame,on="movie_id")


# In[258]:


dframe.groupby(dframe['title']).mean().sort_values('rating',ascending=False).head()


# In[259]:


dframe.groupby(dframe['title']).count().sort_values("rating",ascending=False)


# In[260]:


rating=pd.DataFrame(dframe.groupby(dframe['title']).mean()["rating"])


# In[261]:


rating.head()


# In[262]:


rating["count of rating"]=pd.DataFrame(dframe.groupby(dframe['title']).count()["rating"])


# In[263]:


rating.head()


# In[264]:


rating.sort_values(by="rating",ascending=False)


# In[265]:


plt.figure(figsize=(10,6))
plt.hist(rating["count of rating"],bins=70)
plt.show()


# In[266]:


plt.hist(rating["rating"],bins=70)
plt.show()


# In[267]:


sns.jointplot(x='rating',y='count of rating',data=rating,alpha=0.5)


# In[268]:


dframe.head()


# In[269]:


mov=dframe.pivot_table(index="user_id",columns="title",values="rating")


# In[270]:


mov.head()


# In[271]:


rating.sort_values("count of rating",ascending=False)


# In[272]:


starwars_ratings=mov["Star Wars (1977)"]
starwars_ratings.head()


# In[273]:


similar_to_starwars=mov.corrwith(starwars_ratings)


# In[274]:


corr_starwars=pd.DataFrame(similar_to_starwars,columns=['Correlation'])


# In[275]:


corr_starwars.dropna(inplace=True)


# In[276]:


corr_starwars.head()


# In[278]:


corr_starwars.sort_values("Correlation",ascending=False).head(10)


# In[279]:


corr_starwars=corr_starwars.join(rating["count of rating"])
corr_starwars.head()


# In[281]:


corr_starwars[corr_starwars['count of rating']>100].sort_values('Correlation',ascending=False)


# In[282]:


def recommend (movie_name):
    movie_rating=mov[movie_name]
    similar_to_movie=mov.corrwith(movie_rating)
    corr_movie=pd.DataFrame(similar_to_movie,columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie=corr_movie.join(rating['count of rating'])
    recommend=corr_movie[corr_movie['count of rating']>100].sort_values('Correlation',ascending=False)
    return recommend


# In[288]:


recommend("12 Angry Men (1957)")


# In[ ]:




