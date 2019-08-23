#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
while a:
    drink = input()
    if drink == 'A':
        a -= 18
    elif drink == 'B':
        a -= 28
    elif drink == 'C':
        a -= 10
    elif drink == 'D':
        a -= 50
    elif drink == 'E':
        a -= 89
    if a < 0:
        print(a)
        break
    


# In[ ]:




