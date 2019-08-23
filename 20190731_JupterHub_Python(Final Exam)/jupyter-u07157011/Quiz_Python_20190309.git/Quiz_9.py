#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input())
day = int(0)
while a>0:
    day = day+1
    if (a-15)>0:
        a = a-15
    else:
        print(day, "__1__",a)
        break
    if (a-30)>0:
        a = a-30
    else:
        print(day,"__2__",a)
        break
    if (a-25)>0:
        a = a-25
    else:
        print(day, "__3__",a)
        break


# In[ ]:




