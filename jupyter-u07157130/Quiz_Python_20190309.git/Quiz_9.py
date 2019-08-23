#!/usr/bin/env python
# coding: utf-8

# In[20]:


a=int(input(""))
b=15
c=30
d=25
e=1
f=2
g=3
i=a//(b+c+d)
j=a-i*(b+c+d)
if(j>15):
    i=i+1
if(j<=45 and j>15):
    k=j-15
    print(i,'_',e,'_',k)
elif(j>45 and j<=70):
    k=j-45
    print(i,'_',f,'_',k)
elif(j>70 and j<=85):
    k=j-70
    print(i,'_',g,'_',k)
elif(j<15):
    print(i,'_',g,'_',j)


# In[ ]:





# In[ ]:




