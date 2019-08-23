#!/usr/bin/env python
# coding: utf-8

# In[13]:



a=int(input())
while a>0:
    if a>0 :
        b=input()
        a-=b.count("A")*18
        a-=b.count("B")*28
        a-=b.count("C")*10
        a-=b.count("D")*50
        a-=b.count("E")*89
    
print(a)



    

        


# In[ ]:




