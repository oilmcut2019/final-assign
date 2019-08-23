#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
day = 1
while a>=0:
    a -= 15;b=1
    if a<30:
        break
    a-=30;b+=1
    if a<25:
        break
    a-=25;b+=1
    if a<15:
        break
    day+=1
print (day ,'_',b,'_',a)

