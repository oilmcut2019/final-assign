#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input())
b=0
while a>=70:
    a=a-70
    b+=1
if a>45:
    print(b,2,a-45)
if a>15:
    print(b,1,a-15)
if a<=15:
    print(b,0,a)

    
    


# In[ ]:




