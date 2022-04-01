import pandas as pd

ds = pd.read_csv('C:/Users/prath/Documents/bank.csv')
a = ds.to_excel('bankc.xlsx')
#print(ds.head())
print(a)