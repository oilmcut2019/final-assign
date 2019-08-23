#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=int(input())
i=1
while i<=a:
    b=i % 3
    if b==0:
        print(i)
    i+=1

