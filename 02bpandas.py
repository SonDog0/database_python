import numpy as np
import pandas as pd


# 타이타닉 예제를 이용한 pandas 활용
pd.set_option('display.expand_frame_repr', False)
titanic = pd.read_csv('c:/Java/data/titanic.csv')
# print(titanic.fillna(method='ffill',axis=1))

print(titanic.head(10))
print(titanic.tail(10))


# 타이타닉 데이터 구조 파악
print('데이터 구조 파악 (행,열)',titanic.shape)
print('기술적 통계 파악\n',titanic.shape)

# 타이타닉 데이터 중 1번째 승객 정보 출력
print('첫번째 승객 정보\n',titanic[:1])
print('첫번째 승객 정보\n',titanic.iloc[0])

titanic = titanic.set_index(titanic['Name'])
print('첫번째 승객 정보\n',titanic.loc['Braund, Mr. Owen Harris']) # 1번째 컬럼명 2번째 인덱스 지정한것 확인

print('5~10번째 승객 정보\n',titanic.iloc[4:10])

# 조건 검색하기
print('생존 여부\n', (titanic['Survived']==1).head())
print('생존자\n', (titanic[titanic['Survived']==1]).head())
print('남성 생존자\n', ((titanic['Survived']==1) & (titanic['Sex']=='male')).head())



print('25세 이상 여자승객 생존여부\n', ((titanic['Age'] >= 25)
      & (titanic['Sex']=='female') & (titanic['Survived']==1)).tail())


a = titanic['Age'] >= 25
b = titanic['Sex']=='female'
c = titanic['Survived']==1
print('25세 이상 여자승객 생존여부\n',(a&b&c).tail())
print('25세 이상 여자승객 생존여부\n',(titanic[a&b&c]).head())
print('25세 이상 여자승객 생존여부\n',(titanic[a&b&c][['Age','Sex','Survived']]).head())





# 데이터프레임에 새로운 항목 추가
titan = pd.DataFrame()

titan['Name'] = ['혜교','지현']
titan['Age'] = [38,25]
titan['Sex'] = ['female','male']
print(titan)

person = pd.Series(['수지',23,'female'],index=['Name','Age','Sex'])
titan = titan.append(person, ignore_index=True)
print(titan)


nums = [10,20,30,40,50]
idx = ['a','b','c','d','e']

df = pd.DataFrame(nums, idx)
print('생성된 데이터 프레임', df)

# 데이터프레임에 새로운 열 추가하기
floats = [1.5,2.5,3.5,4.5,5.5]
df['floats'] = floats
print('수정된 데이터 프레임\n', df)

# 컬럼명 수정하기
df.columns = ['ints','floats']
print('수정된 데이터 프레임\n', df)

# 새로운 행을 추가하기
df = df.append({'ints':60, 'floats':6.5},
               ignore_index=True)
print('수정된 데이터 프레임\n', df)


# 새로운 행을 추가하기 , 인덱스 지정
df = df.append(pd.DataFrame({'ints':70, 'floats':7.5},index=[6,]))
print('수정된 데이터 프레임\n', df)


# 데이터프레임 합치기 - join
# 두 데이터프레임을 합치는 기준은 index
# index가 없는 데이터를 합치는 경우 NaN으로 저장
df.index = ['a','b','c','d','e','f','g']
print('수정된 데이터프레임\n', df)

df2 = pd.DataFrame([1,4,9,16,25],
                   index=['a','b','x','y','z'],
                   columns=['newOne'])
print('조인할 데이터 프레임\n', df2)



df3 = df.join(df2)
print('조인된 데이터 프레임\n', df3)

df4 = df.join(df2, how = 'inner')    # 일치하는 인덱스
print('조인된 데이터 프레임\n', df4)

df5 = df.join(df2, how = 'outer')    # 일치하지 않는 인덱스 위주
print('조인된 데이터 프레임\n', df5)

df6 = df.join(df2, how = 'left')    # 일치하지 않는 인덱스 위주
print('left 조인된 데이터 프레임\n', df5)

df6 = df.join(df2, how = 'right')    # 일치하지 않는 인덱스 위주
print('right 조인된 데이터 프레임\n', df5)



# 데이터프레임 시각화
# 데이터프레임의 데이터를 이용해서 간단한 그래프 생성
# matplotlib의 plot 함수를 데이터프레임에 내장시켜
# 언제든 그래프를 그릴 수 있게 해 줌

data1 = [10,20,30,40,50]
data2 = [1.5,2.5,3.5,4.5,5.5]
idx = np.arange(1,6)

df = pd.DataFrame(data1,idx)
df['data2'] = data2
df.columns = ['int','float']
print('시각화용 데이터',df)



# 데이터프레임.plot.그래프 유형
import matplotlib.pyplot as plt

# df.plot()  # 선 그래프
# plt.show()
#
# df.plot.bar()  # 막대 그래프
# plt.show()
#
# df.plot.hist()  # 히스토그램
# plt.show()
#
# df.plot.box()  # 박스 그래프
# plt.show()
#
# df.plot.pie(x='int',y='float')  # 파이 그래프
# plt.show()
#
# df.plot.scatter(x='int',y='float')  # 산점도
# plt.show()

# 데이터셋을 이용한 시각화하기
from sklearn import datasets

iris =datasets.load_iris()
df_iris = pd.DataFrame(iris.data,
                       columns=iris.feature_names)

print(iris.target)

df_iris.plot.scatter(x='petal length (cm)',y='petal width (cm)')
plt.show()

df_iris.plot.scatter(x='sepal length (cm)',y='sepal width (cm)')
plt.show()