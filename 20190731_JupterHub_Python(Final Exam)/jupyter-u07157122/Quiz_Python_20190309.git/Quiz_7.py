#!/usr/bin/env python
# coding: utf-8

# In[45]:


a=input()
a = a.split()
for x in range(0,3):
    a[x] = float(a[x])

for x in range(0,3):
    for y in range(0,3):
        swap = 0
        if a[x]<a[y]:
            swap = a[x]
            a[x] = a[y]
            a[y] = swap

print(a[1]*a[2])


# In[24]:


a[1]

