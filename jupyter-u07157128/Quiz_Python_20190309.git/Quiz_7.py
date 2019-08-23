#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = float (input())
b = float (input())
c = float (input())
if c<a and c<b:
    print(a*b)
elif b<a and b<c:
    print(a*c)
elif a<b and a<c:
    print(b*c)

