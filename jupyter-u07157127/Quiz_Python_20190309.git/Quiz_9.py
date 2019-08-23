#!/usr/bin/env python
# coding: utf-8

# In[20]:


a=int(input())
d=0
t=0
while a>0:
        d+=1
        a-=15
        if a<30:
            t=1
            break;
        else:  
            a-=30
            
            if a<25:
                t=2
                break;
            else:
                a-=25
                
                if a<15:
                    t=3
                    break;
                    

                    
print(d,"_",t,"_",a)
    


# In[ ]:




