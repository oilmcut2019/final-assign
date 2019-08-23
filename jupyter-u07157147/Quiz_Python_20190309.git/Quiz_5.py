#!/usr/bin/env python
# coding: utf-8

# In[2]:


season = [[3,4,5],[6,7,8],[9,10,11],[12,1,2]]

number = int(input('key the month : '))
if number in season[0][0:3]:
    print('Spring')
elif number in season[1][0:3]:
    print('Summer')
elif number in season[2][0:3]:
    print('Fall')
elif number in season[3][0:3]:
    print('Winter')
else:
    print('not month')

