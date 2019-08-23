#!/usr/bin/env python
# coding: utf-8

# In[1]:


month = int(input('month:'))
season = [[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if month in season[0][0:3]:
        print('winter')
if month in season[1][0:3]:
        print('spring')
if month in season[2][0:3]:
        print('summer')
if month in season[3][0:3]:
        print('fall')


# In[ ]:




