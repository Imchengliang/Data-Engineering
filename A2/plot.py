#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('part-r-00000.txt', dtype=str)
l1, l2, l3 = [], [], []
for i in data:
    l1.append(i[0])
    l2.append(int(i[1]))
'''
for i in range(len(data)):
    l4 = []
    l4.append(l1[i])
    l4.append(l2[i])
    l3.append(l4)
'''
plt.bar(l1, l2)
plt.title('number of words starting with each letter')
plt.show()
