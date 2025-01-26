import numpy as np
import pandas as pd

#SERIES
# print(pd.Series(data=[1,2],index=['a','b']))
# print(pd.Series(data=np.array([1,2]),index=['a','b']))
# print(pd.Series(data={'a':1,'b':2},index=['a','b']))

#DF
# df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
# print(df[['W','Z']])
# print(df['W'] + df['Y'])
# print(df.drop('Z',axis=1,inplace=False))
# print(df.loc[['A','B'],['W','Y']])

#NA
# df = pd.DataFrame({'A':[1,2,np.nan],
#                    'B':[5,np.nan,np.nan],
#                    'C':[1,2,3]})
# print(df.dropna(thresh=2,axis=1))
# print(df['A'].fillna(value=df['A'].mean()))
# print(df.fillna(value=df.mean()))

#DATA
# df = pd.DataFrame({'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#                    'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
#                    'Sales':[200,120,340,124,243,350],
#                    'Sales2':[200,120,340,124,243,350]})
# print(df.groupby('Company').mean())
# print(df.groupby('Company').describe()['Sales']['std']['GOOG'])
# print(df.groupby('Company').describe().transpose()['GOOG']['Sales']['std'])

#CONCAT
# df1 = pd.DataFrame(data={'A':['A0','A1'],
#                          'B':['B0','B1']}, index="0 1".split())
# df2 = pd.DataFrame(data={'A':['A2','A3'],
#                          'B':['B2','B3']}, index="2 3".split())
# print(pd.concat([df1,df2]))
# print(pd.concat([df1,df2],axis=1))

#MERGE
l = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K30'],
                       'A': ['A0', 'A1', 'A2', 'A3'],
                       'B': ['B0', 'B1', 'B2', 'B3']})   
r = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})    
print(pd.merge(left,right,how='inner',on='key'))