#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=int(input())
b=int(input())
c=int(input())
if a>b:
    if b>c:
        print(a*b)
    else:
        print(a*c)
if b>c:
    if a>c:
        print(a*b)
    else:
        print(b*c)
if c>a:
    if a>b:
        print(c*a)
    else:
        print(b*c)



# In[ ]:




