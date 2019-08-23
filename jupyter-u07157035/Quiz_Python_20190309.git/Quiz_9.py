#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=int(input())
x=1
while a>=70:
    a=a-70
    x+=1
if 15<=a<45:
    a=a-15
    y=1
elif 45<=a<70:
    a=a-30
    y=2
else:
    y=0
print(x,"_",y,"_",a)

