#!/usr/bin/env python
# coding: utf-8

# In[12]:


a=int(input())
while a>=0:
    b=input()
    if b=='A':
        a-=18
    elif b=='B':
        a-=28
    elif b=='C':
        a-=10
    elif b=='D':
        a-=50
    elif b=='E':
        a-=89
    if a<=0:
        print(a)
        break


# In[ ]:





# In[ ]:




