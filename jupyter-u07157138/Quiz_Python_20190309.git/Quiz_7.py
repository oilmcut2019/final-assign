#!/usr/bin/env python
# coding: utf-8

# In[20]:


a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a>b and b>c:
    print(a*b)
elif b>a and a>c:
    print(b*a)
elif c>a and a>b:
    print(c*a)
elif a>c and c>b:
    print(a*c)
elif b>c and c>a:
    print(b*c)
elif c>b and b>a:
    print(c*b)


# In[ ]:




