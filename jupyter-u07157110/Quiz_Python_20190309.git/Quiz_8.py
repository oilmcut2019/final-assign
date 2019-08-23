#!/usr/bin/env python
# coding: utf-8

# In[1]:


#先輸入1個正整數表示目前的數值，再連續輸入多個 A~E之間任意的英文字母，
#當輸入A時，將目前數值 減去 18
#當輸入B時，將目前數值 減去 28
#當輸入C，將目前數值 減去10
#當輸入D，將目前數值 減去 50
#當輸入E，將目前數值 減去 89
#直到目前數值小於零時，印出小於零的最終數值
a=int(input())
x=1
while a>0:
    b=input()
    if b=="A":
        a-=18
    elif b=="B":
        a-=28
    elif b=="C":
        a-=10
    elif b=="D":
        a-=50
    elif b=="E":
        a-=89
        
print(a)


# In[ ]:




