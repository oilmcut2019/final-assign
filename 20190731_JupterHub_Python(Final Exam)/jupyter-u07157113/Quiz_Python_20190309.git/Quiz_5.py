#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=int(input())
season =[[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if a in season[0][0:3]:
    print('winter')
if a in season[1][0:3]:
    print('spring')
if a in season[2][0:3]:
    print('summer')
if a in season[3][0:3]:
    print('fall')


# In[ ]:




