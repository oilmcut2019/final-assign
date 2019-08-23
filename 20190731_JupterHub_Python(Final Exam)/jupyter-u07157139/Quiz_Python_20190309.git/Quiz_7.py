#!/usr/bin/env python
# coding: utf-8

# In[1]:


A=float(input("A="))
B=float(input("B="))
C=float(input("C="))
if A>B>C:
    print(A*B)
elif A>C>B:
    print(A*C)
elif B>A>C:
    print(B*A)
elif B>C>A:
    print(B*C)
elif C>A>B:
    print(C*A)
elif C>B>A:
    print(C*B)
else:
    print("X")


# In[ ]:




