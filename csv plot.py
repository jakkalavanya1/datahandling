import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.pyplot import xlim
#filename = 'C:/Users/LAVANYA/Desktop/data_12_20_17__10_41_42.csv'
filename = 'F:/UNIVERSITY OF DELAWARE/lab/line following/TZ6.csv'
reader = csv.reader(open(filename))
datMat = list(reader) #list of lists is the output
entries = len(datMat)
#print(datMat)
#print(entries)
#now take first column as time
#np_time = np.array(datMat[:,0])
#time = datMat[:,0]
#print(type(datMat))
#print(datMat[:][0])
time = []
for row in datMat:
    if row[1]=='6':
        time.append(row[0])
print(time)
#print(time.size())
index = []
for row in datMat:
    if row[1]=='6':
        index.append(row[1])
print(index)
plt.plot(time,index)
#plt.ylim(1,5)
plt.show()
#print(index.sort(key=None,reverse=True))
#np_index = np.array(index)
rows = zip(time,index)
with open('F:/UNIVERSITY OF DELAWARE/lab/line following/data_%s.csv' %f, "w"):
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
f.close()