#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input())
x=int(15)
y=int(30)
z=int(25)
day=1
while(a>=0):
    a-=x;b=1
    if(a<y):
        break
    a-=y;b+=1
    if(a<z):
        break
    a-=z;b+=1
    if(a<x):
        break
    day+=1
    
print(day,'_',b,'_',a)


# In[ ]:




