#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=float(input())
b=float(input())
c=float(input())
if a>b:
    if b>c:
        print(a*b)
    else:
        print(a*c)
else:
    if a>c:
        print(b*a)
    else:
        print(b*c)


# In[ ]:




