#!/usr/bin/env python
# coding: utf-8

# In[10]:


g11 = int(input("paper= "))
if g11>100:
    g41=g11//70
    g36=g11%70  
    if g36<15 :
        kar = 3
    elif g36 <45:
        kar=1
    elif g36<70:
        kar=2    
    
    if g36-15<0 :
        g3 =g36
    elif g36-40<0:
        g3 = g36-15
    elif g36-70<0:
        g3 = g36-40
    
    
    
    print(g36)    
    
    print(g41,"_",kar,"_",g3 )
print("paper is to lost")


# In[ ]:





# In[ ]:




