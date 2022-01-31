#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Equação do segundo grau
import math #importa a biblioteca de matemática

def raiz_equação(a, b, c):
    if a == 0:
        print('Como a é 0, isso não é uma equação do segundo grau!')
    else:
        delta = b*b - (4*a*c)
    
        if delta < 0:
            print('A equação possui duas raizes imaginárias!')
        elif delta == 0:
            x = -b/(2*a)
            print(f'A equação possui uma raiz real igual a {x}')
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print(f'A equação possui duas raizes reais e iguais a \nx1={x1}\nx2={x2}')
            
raiz_equação(4,2,0)


# In[ ]:




