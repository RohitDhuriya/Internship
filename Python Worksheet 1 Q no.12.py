#!/usr/bin/env python
# coding: utf-8

# Write a pyhton program to find whether a number is prime or composite

# In[ ]:


num=int(input('Enter the natural number:'))
if num<1:
    print('Number needs to be greater than 1')
elif num==1:
    print(num,'Neither prime nor composite')
else:
    for divisor in range(2,(num//2)+1):
        if(num%divisor)==0:
            print(num,'is a composite number')
            break
    else:
        print(num,'is a prime number')


# In[ ]:




