#!/usr/bin/env python
# coding: utf-8

# In[6]:


X = int(input("輸入正整數="))

while X >= 0 :
    Y = str(input("輸入A~E:"))
    if Y =="A":
            X -= 18
    elif Y =="B":
            X -= 28
    elif Y =="C":
            X -= 10
    elif Y =="D":
            X -= 50
    elif Y =="E":
            X -= 89
    else:
            X += 0

print(X)


# In[ ]:





# In[ ]:




