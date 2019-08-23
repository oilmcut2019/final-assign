#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
第1份訂單用紙量 : 15張

第2份訂單用紙量 : 30張

第3份訂單用紙量 : 25張 
'''
paper=int(input())
a=paper%70
if (a%70==0):
    x=paper//70
elif (a<15):
    x=paper//70
else:
    x=paper//70+1
if (a<15):
    b=3
    c=a
if(15<a<45):
    b=1
    c=a-15
if (45<a<70):
    b=2
    c=a-45
print(x,'_',b,'_',c)


# In[ ]:




