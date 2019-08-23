#!/usr/bin/env python
# coding: utf-8

# In[21]:


a=int(input("a="))
b=int(input("b="))
if(a>b):
    for x  in range(b,a+1) :
        print(x)
else:
    for x in range(a,b+1):
        print(x)
        

