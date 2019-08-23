#!/usr/bin/env python
# coding: utf-8

# In[27]:


a = input().split()
sum = float()
now = float()
for x in range(0,int(a[0])):
    now = float(a[1]) + (float(a[1])/2)*x
    sum = sum + now
print(sum)

