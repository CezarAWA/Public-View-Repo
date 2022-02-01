#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Importing math library #
import math 

# Asking for the value of "a" #
a = int(input('Please, provide the value of "a": '))

# Analisyng the value of "a" and delta and asking for the value of "b" and "c" #
if a == 0:
    print('Since "a" is equal to 0, this is not a second-degree equation!')
else:
    b = int(input('Please, provide the value of "b": '))
    c = int(input('Please, provide the value of "c": '))
    
    delta = b*b - (4*a*c)
    
    if delta < 0:
        print('The equation has two imaginary roots!')
    elif delta == 0:
        x = -b/(2*a)
        print(f'The equation has one real root equal to {x}.')
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f'The equation has two real roots, x1={x1} and x2={x2}.')

