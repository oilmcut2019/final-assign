#!/usr/bin/env python
# coding: utf-8

# In[ ]:


now = 0
go = object()
first = False

while(1):
    if first == False:
        now = int(input())
        first = True
        if (now <= 0):
            break
    else:
        go = input()
        if go == 'A':
            now -= 18
        elif go == 'B':
            now -= 28
        elif go == 'C':
            now -= 10
        elif go == 'D':
            now -= 50
        elif go == 'E':
            now -= 89
        

        if (now <= 0):
            break

print(now)
            
#當輸入A時，將目前數值 減去 18

#當輸入B時，將目前數值 減去 28

#當輸入C，將目前數值 減去10

#當輸入D，將目前數值 減去 50

#當輸入E，將目前數值 減去 89


# In[ ]:




