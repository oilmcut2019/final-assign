#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = float(input())
b = float(input())
c = float(input())

if a>b and a>c:
    if b>c:
        num = a*b
        print(num)
    else:
        num = a*c
        print(num)
elif b>a and b>c:
    if a>c:
        num = b*a
        print(num)
    else:
        num = b*c
        print(num)
else:
    if a>b:
        num = c*a
        print(num)
    else:
        num = c*b
        print(num)


# In[ ]:




