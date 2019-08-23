#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=int(input("x="))
day=1
while x>0:
    x=x-15;y=1
    if x<30:
        break
    x=x-30;y=y+1
    if x<25:
        break
    x=x-25;y=y+1
    if x<15:
        break
    day=day+1
print(day,'_',y,'_',x)


# In[ ]:




