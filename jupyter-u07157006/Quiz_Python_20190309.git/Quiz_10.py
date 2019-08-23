#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = int(input())
b = float(input())
i=0
d=0
q=a-1
while i<=q:
    c=b+b/2*(i)
    d+=c
    i+=1
    
print("%.2f" % d)    


# In[ ]:




