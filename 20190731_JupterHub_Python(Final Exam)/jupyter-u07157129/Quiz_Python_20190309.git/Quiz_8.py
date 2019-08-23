#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("a="))
while (a>0):
    b=str(input("b="))
    if b=="A":
        a=a-18
    elif b=="B":
        a=a-28
    elif b=="C":
        a=a-10
    elif b=="D":
        a=a-50
    elif b=="E":
        a=a-89
print(a)

