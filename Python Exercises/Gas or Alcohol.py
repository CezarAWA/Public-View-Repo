#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Defining a list with the price of alcohol and gas #
pc = [1.90,2.50]

# Asking the user wich fuel will be chosen #
print(f'Please, choose fuel: [0]Alcohol [1]Gas:')
c=input()
c=int(c)

# Asking the user how much fuel is wanted # 
print(f'Please, type fuel quantity in liters:')
nl=float(input())

# Calculating and printing total value #
V = nl * pc[c]
print(f'The total value is: R${V}.')


# In[ ]:




