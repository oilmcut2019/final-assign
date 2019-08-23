#!/usr/bin/env python
# coding: utf-8

# In[7]:


n=int(input())
x=float(input())
ans=0
while n!=0:
    sum=x+x/2*(n-1)
    ans=ans+sum
    n-=1
print("%.2f"%ans)


# In[ ]:





# In[ ]:




