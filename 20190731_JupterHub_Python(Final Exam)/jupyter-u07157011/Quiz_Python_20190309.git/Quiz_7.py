#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
b = int(input())
c = int(input())

ans = 0
if a>b:
    if a>c:
        t=a
if b>a:
    if b>c:
        t=b
if c>a:
    if c>b:
        t=c
if t>a>b:
    t2=a
if t>a>c:
    t2=a
if t>b>c:
    t2=b
if t>b>a:
    t2=b
if t>c>b:
    t2=c
if t>c>a:
    t2=c   
ans=t*t2
print(ans)
        
        


# In[ ]:




