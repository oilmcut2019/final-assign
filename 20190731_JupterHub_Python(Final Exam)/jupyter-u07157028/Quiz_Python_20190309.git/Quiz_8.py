#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = int(input("coin"))
while a>0:
    b = input()
    if b == "A":
        a = a-18
    elif b == "B":
        a = a-28
    elif b == "C":
        a = a-10
    elif b == "D":
        a = a-50
    else:
        a = a-89
print(a)


# In[ ]:





# In[ ]:




