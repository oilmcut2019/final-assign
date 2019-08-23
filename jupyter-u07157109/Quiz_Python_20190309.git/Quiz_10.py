#!/usr/bin/env python
# coding: utf-8

# In[14]:


N=float(input("樓層高度:"))
X=float(input("1樓的巡察時間:"))
Y=X/2
Z=1
A=2
B=0

while Z <=N :
    if Z == 1:
        sum=X
        Z+=1
    else:
        sum=sum+X+Y
        B=Z-1
        Y=Y*B
        Z+=1
    
print(sum)


# In[ ]:





# In[ ]:




