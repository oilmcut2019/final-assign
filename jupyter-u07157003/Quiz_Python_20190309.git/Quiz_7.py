#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if(a > b > c):
    print(a*b)
if(a > c > b):
    print(a*c)
if(b > a > c):
    print(a*b)
if(b > c > a):
    print(c*b)
if(c > b > a):
    print(c*b)
if(c > a > b):
    print(a*c)


# In[ ]:




