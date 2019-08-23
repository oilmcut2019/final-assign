#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=float(input())
b=float(input())
c=float(input())
if(a>b and a>c):
    if(b>c):
        print(a*b)
    else:
        print(a*c)
elif(b>a and b>c):
    if(a>c):
        print(b*a)
    else:
        print(b*c)
else:
    if(a>b):
        print(a*c)
    else:
        print(b*c)


# In[ ]:




