#!/usr/bin/env python
# coding: utf-8

# In[24]:


a=int(input())
d=0
s=0
p=0
x=100
while x>0:
    d+=1
    a-=15
    if a>0:
        s=1
        p=a
        a-=30
        if a>0:
            s=2
            p=a
            a-=25
            if a>0:
                p=a
                s=3
            else:
                print(d,s,p,sep="_")
                x=0
        else:
            print(d,s,p,sep="_")
            x=0
    else:
        print(d,s,p,sep="_")
        x=0
        
    
    


# In[ ]:




