#!/usr/bin/env python
# coding: utf-8

# In[8]:


a = int(input("paper number"))
day = int(0)
while a>0:
    day = day+1
    if (a-15)>0:
        a = a-15
    else:
        print(day,"_1_",a)
        break
    if (a-30)>0:
        a = a-30
    else:
        print(day,"_2_",a)
        break
    if (a-25)>0:
        a = a-25
    else:
        print(day,"_3_",a)
        break
        


# In[ ]:




