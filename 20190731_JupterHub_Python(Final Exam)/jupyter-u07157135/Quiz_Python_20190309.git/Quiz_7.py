#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = float(input())
b = float(input())
c = float(input())
if a>b:
    if a>c:
        if b>c:
            print(a*b)
        else:
            print(a*c)
    else:
            print(b*c)
else:
    if a>c:   
            print(a*b)
    else:
            print(b*c)
    


# In[ ]:




