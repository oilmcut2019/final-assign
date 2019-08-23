#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=float(input())
b=float(input())
c=float(input())
if a<b and a<c:
    print(b*c)
elif b<c and b<a:
    print(c*a)
elif b>c and c<a:
    print(b*a)

