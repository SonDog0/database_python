import numpy as np
import pandas as pd


# pandas 입출력
pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('c:/java/ddrdata/cluster.csv',
                    encoding='euc-kr')

# print(df)

# print(df.iloc[5][10])
#
# print(len(df))

temp = []
strr = ''

for i in range(0,len(df)):
    if df.iloc[i][10] == 1:
        strr += 'D'
    if df.iloc[i][11] == 1:
        strr += 'F'
    if df.iloc[i][12] == 1:
        strr += 'L'
    if df.iloc[i][13] == 1:
        strr += 'N'
    if df.iloc[i][14] == 1:
        strr += 'O'
    if df.iloc[i][15] == 1:
        strr += 'P'
    if df.iloc[i][16] == 1:
        strr += 'Q'
    if df.iloc[i][17] == 1:
        strr += 'R'
    if df.iloc[i][18] == 1:
        strr += 'S'
    temp.append(strr)
    strr = ''

print(temp)

df["category"] = temp

print(df)



df.to_csv('cluster_category.csv',sep=',' , encoding='UTF-8')