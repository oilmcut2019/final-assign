#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("floor"))
x = float(input("time"))
cnt = int(0)
ft = float(x)
t=float(0)
while cnt<n:
    t=t+ft
    cnt=cnt+1
    ft=ft+(x/2)
print(t)



# In[ ]:




