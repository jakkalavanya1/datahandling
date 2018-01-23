import numpy as np
import matplotlib.pyplot as plt
import csv
a = [[1,2,3],[4,5,6],[7,8,9]]
#print(a[:][0])
#zip(*a)
col = []
for row in a:
    if row[1]==2:
        col.append(row[0])
print(col)
#print(col.sort())