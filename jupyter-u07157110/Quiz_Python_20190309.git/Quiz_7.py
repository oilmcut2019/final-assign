#!/usr/bin/env python
# coding: utf-8

# In[11]:


a=float(input())
b=float(input())
c=float(input())
if a>b:
    if b>c:
        a*=b
        print(a)
    elif b<c:
        a*=c
        print(a)
elif a<b:
    if a>c:
        b*=a
        print(b)
    elif a<c:
        b*=c
        print(b)

