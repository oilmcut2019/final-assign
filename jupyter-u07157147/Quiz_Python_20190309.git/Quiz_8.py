#!/usr/bin/env python
# coding: utf-8

# In[9]:


money = int(input('input the number : '))
total = money
print('Total :',total)

while total > 0:
    if total > 0:
        item = input()
        total -= item.count('A')*18
        total -= item.count('B')*28
        total -= item.count('C')*10
        total -= item.count('D')*50
        total -= item.count('E')*89
print(total)        


# In[ ]:




