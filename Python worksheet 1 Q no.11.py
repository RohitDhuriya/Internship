#!/usr/bin/env python
# coding: utf-8

# Write a python program to find the factorial of a number?

# In[ ]:


fact=1
num=int(input('Enter the number:'))
org=num
while num>0:
    fact=fact*num
    num=num-1
print('The factorial of ',org,'is',fact)


# In[ ]:




