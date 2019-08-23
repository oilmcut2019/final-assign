#!/usr/bin/env python
# coding: utf-8

# In[30]:


'''
問題描述 : 計算3個數當中，最大的數 與 第二大的數 的乘積。

輸入 : 任意輸入3個相異的數。

輸出 :

最大的數 與 第二大的數 的乘積
1.6689 100.0 3.773 
'''
max=0
sec=0
a=float(input());b=float(input());c=float(input())
if a>b>c or a>c>b:
    max=a
elif b>a>c or b>c>a:
    max=b
elif c>a>b or c>b>a:
    max=c
    
if b>a>c or c>a>b:
    sec=a
elif a>b>c or c>b>a:
    sec=b
elif a>c>b or b>c>a:
    sec=c

print(max*sec)


# In[ ]:




