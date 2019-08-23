#!/usr/bin/env python
# coding: utf-8

# In[2]:


high = int(input())
time = float(input())
a = 1 ; b = 1 ; total = 0 
while a<=high:
    if a == 1:
        total += time
        a += 1
    else:
        total+=time+(time/2)*b
        b+=1
        a+=1
print(total)

