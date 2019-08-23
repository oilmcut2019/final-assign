#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=float(input(""))
b=float(input(""))
c=float(input(""))
if(a>b and a>c ):
    if b>c :
        i=a*b
        print(i)
    else:
        i=a*c
        print(i)
elif(b>a and b>c ):
    if a>c:
        k=b*a
        print(k)
    else:
        k=b*c
        print(k)
elif(c>a and c>b):
    if (a>b):
        j=a*c
        print(j)
    else:
        j=b*c
        print(j)


# In[ ]:





# In[ ]:




