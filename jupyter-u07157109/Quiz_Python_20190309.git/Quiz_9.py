#!/usr/bin/env python
# coding: utf-8

# In[32]:


x = int(input("目前可用的紙張數量:"))
d=1
s=0
p=0
y=100
while y>0 :
    x-=15
    if x>0:
        s=1
        p=x
        x-=30
        if x>0:
            s=2
            p=x
            x-=25
            if x>0:
                p=x
                d+=1
                s=3
            else:
                print(d,s,p)
                y=0
        else:
            print(d,s,p)
            y=0
    else:
        print(d,s,p)
        y=0


# In[ ]:





# In[ ]:




