#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
b = a%70
if (a%70 == 0):
    x = a/70
elif(b<15):
    x = a/70
else:
    x = a/70 + 1
    
if (b<15):
    y = 3
    z = b
if (15 < b < 45):
    y = 1
    z = b - 15
if (45 < b < 70):
    y = 2
    z = b - 45
print(int(x),"_",y,"_",z)


# In[ ]:




