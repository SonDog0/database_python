# pandas
# 행에 '열 레이블index'를 부착한 다차원 행렬인
# 데이터 프레임 자료구조를 제공하는 패키지
# 핵심요소는 dataframe, series시계열, index지수

# pandas의 창시자 중 한명은 해지펀드 애널리스트로 일하며
# 파이썬에서 금융 시계열자료를 다루기 위한 목적으로 개발

# numpy 기반 행렬은 산술연산에 적합한 자료구조
# pandas 는 numpy 행렬을 대상으로 data munging/wrangling(전처리)
# 시간을 줄여주는 효과가 있음

# data munging/wrangling : data preprocessing
# 원자료를 또 다른 형태의 자료로 변환하거나
# 매핑하는 작업을 의미

import numpy as np
import pandas as pd


# 간단한 시계열 자료 생성
# 시간적인 흐름에 따라 기록한 데이터
# 통계량의 변화가 시간의 움직임에 따라 발생함
# a = pd.Series([0.0,0.25,0.5,0.75,1.0])
# print('시계열자료\n',a)
# print('시계열 자료값\n',a.values)
# print('시계열 인덱스 값\n',a.index)
# print('시계열 2번 자료\n',a[2])
# print('시계열 3,4번 자료\n',a[3:5])
#
#
# # 문자 인덱스를 이용해서 시계열자료 다루기
# b = pd.Series([0.0,0.25,0.5,0.75,1.0],
#               index=['a','b','c','d','e'])
# print('시계열자료\n',b)
# print('시계열 자료값\n',b.values)
# print('시계열 인덱스 값\n',b.index)
# print('시계열 2번 자료\n',b[2])
# print('시계열 b번 자료\n',b['b'])
# print('시계열 3,4번 자료\n',b[3:5])
#
#
#
# # pandas에서 정수형 인덱스를 사용하는 경우
# # 파이썬의 slice 연산과 혼동될 위험이 존재
# # 따라서, pandas만의 특별한 인덱싱indexer 기능을 제공
#
# # iloc : 정수형 인덱스로 요소를 찾음
# # loc : 문자형 인덱스로 요소를 찾음
# # ix : 정수형/문자형 인덱스로 요소를 찾음
#
#
#
# c = pd.Series(['a','b','c','d','e'],
#               index=[1,3,5,7,9])
#
# print('1번데이터\n',c[1])
# print('2~3번 데이터\n',c[2:4])
#
# print('#1번데이터\n',c.loc[1])  # pandas indexer
# print('#2~#3번 데이터\n',c.loc[3:5])
# print('2~3번 데이터\n',c.iloc[2:4])  # python indexer
#
#
#
# # 간단한 데이터프레임 자료 생성
# # 파이썬 딕셔너리의 특수한 형태
# # 시계열이 인덱스를 가진 1차원 배열이라면(벡터)
# # 데이터프레임은 행과 열이름을 가진 2차원 배열(행렬)
# area = {'seoul': 423967,
#         'pusan': 170312,
#         'daejeon': 149995,
#         'inchoun': 141297,
#         'kwangju': 120163}
#
# pop = {'seoul': 38332521,
#         'pusan': 26448193,
#         'daejeon': 19651127,
#         'inchoun': 19552860,
#         'kwangju': 12882135}
#
# states = pd.DataFrame({'pop':pop,
#                        'area':area})
#
# print('지역정보\n', states)
# print('면적정보\n', states['area'], states.area)
# print('인구정보\n', states['pop'], states.pop)
# print('지역정보 인덱스\n', states.index)
# print('지역정보 컬럼\n', states.columns)
#
#
# # 리더쉽 데이터를 pandas DF로 생성하기
# data = {'manager':[1,2,3,4,5],
#         'date':['10/24/14','10/28/14','10/01/14','10/12/14','05/01/14'],
#         'country':['US','US','US','UK','UK'],
#         'gender' : ['M','F','F','M','F'],
#         'age':[32,45,25,39,99],
#         'q1':[5,4,5,5,5],
#         'q2': [3,5,2,5,5],
#         'q3': [3,5,5,5,2],
#         'q4': [3,3,4,0,0],
#         'q5': [2,2,1,2,1]}
# idx = np.arange(1,6)
# leadership = pd.DataFrame(data,index=idx)
#
# print('리더쉽 DF\n', leadership)
# print('나이 컬럼은?\n',leadership.age)
# print('질문 컬럼은?\n',leadership.iloc[:,5:10])
# print('질문 컬럼은?\n',leadership.loc[:,'q1':'q5'])
# print('질문 컬럼은?\n',leadership.ix[:5,'q1':'q5'])
#
#
# # ex)
# df = pd.DataFrame(np.arange(1,26).reshape(5,5),
#                   index=list('abcde'), # 문자형 인덱스
#                   columns=['x','y','z','10','20'])
# print(df)
# print('a/b/c행,10/20열 출력\n',df.iloc[:3,3:5])
# print('a/b/c행,10/20열 출력\n',df.loc[:'c','10':'20'])
# print('a/b/c행,10/20열 출력\n',df.ix[:3,'10':'20'])




# pandas 입출력
# 데이터 파일을 읽어 데이터 프레임을 생성
# csv, excel, json, ... ... 등등 지원

phone = pd.read_csv('c:/Java/data/phoneinfo.csv',
                    encoding='euc-kr')
print('휴대폰사용현황\n',phone)




cols = ['year','buy','display','age','height','weight','hptime','comtime','datatime']
idx = np.arange(1,25)

phone = pd.read_csv('c:/Java/data/phoneinfo.csv',
                    sep=',', names=cols,
                    skiprows=1,header=None,
                    encoding='euc-kr')
phone.index = idx
pd.set_option('display.max_columns',50)
# pd.set_option('display.width',100)
print('휴대폰사용현황\n',phone)


# 데이터 프레임 기본 정보 확인
print(phone.describe())   # R의 summary와 같은 기능
print(phone.head())
print(phone.tail())







cols = ['우편번호','시도','시군구','읍면','도로명','건물번호본번','건물번호부번','시군구용건물명','법정동명','리명','지번본번']
zipcode = pd.read_csv('c:/Java/data/Seoul-2017.10.csv',
                      sep=',', names=cols,
                      skiprows=1, header=None,
                      encoding='utf-8')
#
# # 누락된 데이터 처리 1 : np.nan
# zipcode['읍면'] = zipcode['읍면'].replace(np.nan, '')
# zipcode['리명'] = zipcode['리명'].replace(np.nan, '')




# 누락된 데이터 처리 2 : fillna
# zipcode = zipcode.fillna('')
zipcode.fillna('',inplace=True)    # 수정사항 바로 적용


# print('서울우편번호\n', zipcode)
print(zipcode.describe())
print(zipcode.head())
print(zipcode.tail())


# 누락된 데이터 다루기 - null, NaN, NA, None
# 파이썬/pandas 에서는 NaN(float) 또는 None(object)으로 취급
# 단, 정수형 누락값인 NA는 pandas에서는 취급 불가

# val1 = np.array([1,2,None,4,5])
# print('누락된 데이터',val1)
# print('누락된 데이터 유형',val1.dtype)
# # print('누락된 데이터 산술연산',val1.sum()) # 오류 발생
# # print('누락된 데이터 산술연산',val1*100) # 오류 발생
#
#
# # val1 = np.array([1,2,NaN,4,5])   - 오류 발생
# val2 = np.array([1,2,np.nan,4,5])
# print('누락된 데이터',val2)
# print('누락된 데이터 유형',val2.dtype)
# print('누락된 데이터 산술연산',val2.sum())  # nan 출력
# print('누락된 데이터 산술연산',val2*100)    # nan 빼고 다 적용됨
#
#
# val3 = pd.Series([1,2,np.nan,4,None])
# print('누락된 데이터',val3)
# print('누락된 데이터 유형',val3.dtype)  # None -> nan
# print('누락된 데이터 산술연산',val3.sum())   # 누락값 제외하고 연산이됨
# print('누락된 데이터 산술연산',val3*100)     # nan 빼고 다 적용됨




# null 다루기
# pandas 자료구조에서는 null값을 감지하고 삭제하는 기능 제공
val4 = pd.Series([1,2,np.nan,4,None])
print('널값 출력',val4.isnull())  # null 여부 확인
print('정상값 출력1',val4[val4.notnull()])
print('정상값 출력2',val4[~val4.isnull()])

print('널값 제거\n',val4.dropna())


val5 = pd.DataFrame([[1,np.nan,3],
                     [np.nan,8,10],
                     [15,20,18]])

print(val5.isnull())
print(val5[val5.notnull()])

print(val5.dropna())
print(val5.dropna(axis=0))
#           => 데이터프레임에서 dropna()를 사용하면
#           => 행기준으로 null이 삭제됨

print(val5.dropna(axis=1))   # 열기반 삭제

# null값 대체 - fillna
print('null값 대체\n',val4.fillna(0))

# method=ffill, method=bfill
# 널값기준 앞/뒤값을 대체 할 수 있음
print('앞의 값으로 null값 대체\n',val4.fillna(method='ffill'))
print('뒤의 값으로 null값 대체\n',val4.fillna(method='bfill'))



print('null값 대체\n',val5.fillna(0))
print('행기준 앞의 값으로 null값 대체\n',val5.fillna(method='ffill',axis=1))
print('열기준 앞의 값으로 null값 대체\n',val5.fillna(method='ffill',axis=0))
print('행기준 뒤의 값으로 null값 대체\n',val5.fillna(method='bfill',axis=1))
print('열기준 뒤의 값으로 null값 대체\n',val5.fillna(method='bfill',axis=0))



# 타이타닉 예제 - null 처리, 생존자 수 확인,
pd.set_option('display.expand_frame_repr', False)
titanic = pd.read_csv('c:/Java/data/titanic.csv')
print(titanic.fillna(method='ffill',axis=1))



summermedal = pd.read_csv('c:/Java/data/summermedals.csv')