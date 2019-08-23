#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
if x>y :
    if y>z:
        print(x*y)
if x>z:
    if z>y:
        print(x*z)
if y>x :
    if x>z:
        print(y*x)
if y>z :
    if z>x:
        print(y*z)
if z>x :
    if x>y:
        print(z*x)
if z>y :
    if y>x:
        print(z*y)


# In[ ]:




