#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Defining a list with the price of alcohol and gas #
pc = [1.90,2.50]

# Asking the User wich fuel will be chosen #
print(f'Please, choose fuel: [0]Alcohol [1]Gas:')
c=input()
c=int(c)

# Asking the User how much fuel is wanted # 
print(f'Please, type fuel quantity in liters:')
nl=float(input())

# Calculating total value with discount and printing #
if c==0 :
    if nl <= 20:
        V = nl * pc[c] * 0.97
        print(f'The total value is: R${V}.')
    else:
        V = nl * pc[c] * 0.95
        print(f'The total value is: R${V}.')
else:
    if nl <= 20:
        V = nl * pc[c] * 0.96
        print(f'The total value is: R${V}.')
    else:
        V = nl * pc[c] * 0.94
        print(f'The total value is: R${V}.')


# In[ ]:





# In[ ]:




