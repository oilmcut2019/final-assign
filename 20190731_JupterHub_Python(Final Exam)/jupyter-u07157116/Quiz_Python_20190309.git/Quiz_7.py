#!/usr/bin/env python
# coding: utf-8

# In[3]:


a =float(input("")) 
b =float(input("")) 
c =float(input("")) 
if a>b>c:
    print(a*b)
elif a>c>b:
    print(a*c)
elif b>a>c:
    print(a*b)
elif b>c>a:
    print(c*b)
elif c>a>b:
    print(a*c)
elif c>b>a:
    print(c*b)


# In[ ]:




