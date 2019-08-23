#!/usr/bin/env python
# coding: utf-8

# In[10]:


number1 ,number2 ,number3 = map(float,input('please key :').split())
if number1 > number2:
    if number2 >number3:
        print(number1*number2)
        
    else :
        if number1 > number3:
            if number3 > number2:
                print(number1*number3)
                
elif number2 > number1:
    if number1 > number3:
        print(number2*number1)
        
    else: 
        if number2 > number3:
            if number3 >number1:
                print(number2*number3)
        
elif number3 > number2:
    if number2 > number1:
        print(number3*number2)
    else:
        if number3 > number1:
            if number1 > number2:
                print(number3*number1)


# In[ ]:




