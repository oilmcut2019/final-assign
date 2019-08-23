#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
while a:
    x=input()
    if x=='A':
        a-=18
    elif x=='B':
        a-=28
    elif x=='C':
        a-=10
    elif x=='D':
        a-=50
    elif x=='E':
        a-=89    
    if a<0:
        print(a)
        break

