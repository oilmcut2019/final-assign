#!/usr/bin/env python
# coding: utf-8

# In[11]:


A = int(input("月份="))
B = [[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if A in B[0][0:3]:
    print("winter")
elif A in B[1][0:3]:
    print("spring")
elif A in B[2][0:3]:
    print("summer")
elif A in B[3][0:3]:
    print("fall")
else:
    print("X")


# In[ ]:





# In[ ]:




