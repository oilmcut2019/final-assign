#!/usr/bin/env python
# coding: utf-8

# In[25]:


import code

a = int(input())
day=0;dayly=1;
while(1):
    
    if dayly == 1:
        if (a - 15) <= 0:
            dayly = 1
            break
        else:
            day += 1
            a -= 15
    elif dayly ==2:
        if (a - 30) <= 0:
            dayly -= 1
            break
        else:
            a -= 30
    elif dayly ==3:
        if (a - 25) <= 0:
            dayly -= 1
            day += 1
            break
        else:
            
            a -= 25
            
    if dayly == 3:    
        dayly = 0
        
    dayly += 1
    
print(day,end='_')
print(dayly,end='_')
print(a)
#輸出三個整數，並且用底線當作分隔符號。

#第1個整數：可以使用到第幾天。

#第2個整數：那一天的第幾份訂單完成後，剩餘的張數不足下一份訂單使用。

#第3個整數：最後剩下多少紙張。

        
#第1份訂單用紙量 : 15張

#第2份訂單用紙量 : 30張

#第3份訂單用紙量 : 25張

