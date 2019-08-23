#!/usr/bin/env python
# coding: utf-8

# In[5]:


N = int(input())
X = float(input())
I = X/2
total = 0
for x in range(1,N+1):
    J= X + I*(x-1)
    total += J
print(total)


# In[ ]:




