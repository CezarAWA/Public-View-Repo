#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Creating the lists where the questions and answers will be kept in a string format. #
p = ["Did you call the victim?","Were you at the crime scene?","Do you live near the victim?","Did you owe money to the victim?","Have you ever worked with the victim?"]
a = ["Suspect","Accomplice","Assassin"]

# Creating counter indexes that will be used to pick the strings in the questions list and to keep the answer given by the user. #
i = 0
c = 0

#Loop where the question will be picked in an ascending order from the questions list and the answer will be kept to evaluate if the user is Not Guilty, Suspect, Accomplice or Assasin#
for str in p:
    print(f'{p[c]} [1]Yes ou [0]No ')
    r = input()
    r = int(r)
    c = c + 1
    i = i + r
if i == 2:
    print(f'Evaluation: {a[0]}')
elif i>2 and i<=4:
    print(f'Evaluation: {a[1]}')
elif i == 5:
    print(f'Evaluation: {a[2]}')
else:
    print(f'Evaluation: Not Guilty')

