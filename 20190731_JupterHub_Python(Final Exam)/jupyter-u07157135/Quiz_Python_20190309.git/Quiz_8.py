#!/usr/bin/env python
# coding: utf-8

# In[51]:


total = int(input())
while total >= 0:
    b = str(input())
    if b == "A":
             total-=18
    elif b == "B":
             total-=28
    elif b == "C":
             total-=10
    elif b == "D":
             total-=50
    elif b == "E":
             total-=89
print(total)   


# In[ ]:




