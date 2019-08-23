#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
第一樓7.2分鐘 第四樓(7.2+3.6*3)分鐘

第二樓(7.2+3.6*1)分鐘 總共50.4分鐘

第三樓(7.2+3.6*2)分鐘  
'''
total=0
n=int(input())
first=float(input())
b=first/2
for i in range(1,n+1):
    floor=first+b*(i-1)
    total+=floor
print(total)


# In[ ]:





# In[ ]:




