#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input())

while a>=0:
    b = str(input())
    if b=='A':
        a-=18
    elif b=='B':
        a-=28
    elif b=='C':
        a-=10
    elif b=='D':
        a-=50
    else:
        a-=89

print(a)


# In[ ]:





# In[ ]:




