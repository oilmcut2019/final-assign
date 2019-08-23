#!/usr/bin/env python
# coding: utf-8

# In[24]:


wa2000 =float(input("input"))
iws2000=float(input("input"))
kar98k =float(input("input"))
ak12 = [wa2000,iws2000,kar98k]
g11 = max(ak12)
if max(ak12) ==wa2000:
    if min(ak12) ==iws2000:
        aug = kar98k
if max(ak12) ==wa2000:
    if min(ak12) ==kar98k:
        aug = iws2000
if max(ak12) ==iws2000:
    if min(ak12)==wa2000:
        aug = kar98k
if max(ak12) ==iws2000:
    if min(ak12)==kar98k:
        aug = wa2000

if max(ak12) ==kar98k:
    if min(ak12) ==wa2000:
        aug = iws2000
if max(ak12) ==kar98k:
    if min(ak12) ==iws2000:
        aug = wa2000
an94 = g11*aug    
    
    
print(an94)


# In[ ]:




