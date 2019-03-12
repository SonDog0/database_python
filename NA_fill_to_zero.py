import numpy as np
import pandas as pd


# pandas 입출력
pd.set_option('display.expand_frame_repr', False)
dataframe = pd.read_csv('c:/Java/data/tbl_seoul.csv',
                    encoding='euc-kr')



dataframe.fillna(0,inplace=True)

print(dataframe)

dataframe.to_csv('tbl_seoul_final.csv',sep=',' , encoding='UTF-8')
