#!/usr/bin/env python
# coding: utf-8

# In[1]:


p = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
a = ["Suspeita","Cúmplice","Assasino"]
i = 0
c = 0
for str in p:
    print(f'{p[c]} [1]Sim ou [0]Não ')
    r = input()
    r = int(r)
    c = c + 1
    i = i + r
if i == 2:
    print(f'Avaliação: {a[0]}')
elif i>2 and i<=4:
    print(f'Avaliação: {a[1]}')
elif i == 5:
    print(f'Avaliação: {a[2]}')
else:
    print(f'Avaliação: Inocente')

        


    
        


# # 
