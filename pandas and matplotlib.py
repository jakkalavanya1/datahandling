import numpy as np
import xlrd
import matplotlib.pyplot as plt
import _csv
from xlrd import sheet
location = 'C:/Users/LAVANYA/Desktop/data_12_20_17__10_41_42.csv'
#data = pd.read_csv("F:\UNIVERSITY OF DELAWARE\lab\line following\merging_sorted.csv - merging_sorted.csv")
#brics = pd.read_csv("C:\Users\LAVANYA\Desktop\data_12_20_17__10_41_42.csv")
velocity = [1,2,4,1,4,5]
time = [1,2,3,4,5,6]
xlrd.open_workbook(location ,on_demand=True)
print(sheet.Cell(0,0).value)
#plt.show()
#print(brics)