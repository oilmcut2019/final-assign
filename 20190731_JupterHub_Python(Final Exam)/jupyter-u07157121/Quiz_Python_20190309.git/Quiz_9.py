#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input())
d=1
s=0
p=0
x=100
while x>0:
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
                d+=1
                s=3
            else:
                print(d,"_",s,"_",p)
                x=0
        else:
            print(d,"_",s,"_",p)
            x=0
            else:
                print(d,"_",s,"_",p)
            x=0


# In[ ]:




