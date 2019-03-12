# 파이썬이 제공하는 유용한 자료구조들 중
# 리스트와 딕셔너리가 여러가지 응용분야에서
# 많이 활용되는 핵심요소임

# 하지만, 과학기술이나 금융분야에서는
# 더 빠른 연산이 가능한 특별한 자료구조 필요
# 즉, 선형대수나 벡터공간이론등 수학이론에서 사용되는
# 배열 자료구조가 필요

# n차원의 배열을 쉽고 효율적으로, 고성능으로
# 다루기 위한 목적으로 만들어 짐
# 특히, 디지털 이미지는 해당 영역에 대한 픽셀 정보를
# 2차원 배열로 인식해서 처리할 수 있음
# 데이터가 무엇이든 상관없이 그 데이터를 분석하려면
# 먼저, 숫자배열로 변환하는 것이 우선되어야 함

# n차원 배열
# 파이썬의 리스트와는 달리
# numpy 배열은 같은 종류의 데이터만 저장 가능

import numpy as np

# 파이썬 리스트
a=list([1,2,3,4,5])               # 숫자
b=list(['a','b','c','d','e'])     # 문자
c=list([0.1,'b','c',1,2])         # 실수&문자&정수

# print(type(a),type(b),type(c))
# print(type(a[0]), type(b[0]), type(c[0]), type(c[1]), type(c[3]))

# numpy 배열
# np.array(배열 대상 값들)
d = np.array([1,2,3,4,5])
e = np.array(['a','b','c','d','e'])
f = np.array([0.1,'b','c',1,2])

# print(type(d),type(e),type(f))
# print(type(d[0]), type(e[0]), type(f[0]), type(f[1]), type(f[3]))
#
# print(d.shape)   # 배열의 요소수
# print(d.ndim)    # 벼열의 차원수

g = np.array([[1,2,3],[4,5,6],[7,8,9]])
h = np.array([[ [1,2], [3,4] ], [ [5,6], [7,8] ]])

# print(g.shape)   # 배열의 요소수
# print(g.ndim)    # 벼열의 차원수
#
# print(h.shape)   # 배열의 요소수
# print(h.ndim)    # 벼열의 차원수
#
# # 배열 요소에 접근하기
# print('배열 개별요소 :', d[0],d[2],d[4])
# print('배열 부분요소 :', d[1:3])   # 3번째 요소 안나옴
# print('배열 부분요소 :', d[:3])    # 3번째 요소 안나옴
# print('배열 부분요소 :', d[:])
#
# # 배열 세부정보 확인
# print('차원정보',g.ndim)
# print('요소 수',g.shape)
# print('총 요소 수',g.size)
# print('요소 자료형',g.dtype)
# print('각 요소 자료크기',g.itemsize)
# print('총 요소 자료크기',g.nbytes)

# 난수를 이용한 numpy 배열 생성
# np.random.seed(181214)
# print(np.random.randint(10))  # 0~9사이 난수

x1 = np.random.randint(10,size=6)
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5)) # 4*5 3개 만듬

#print(x1)
#print(x2)
#print(x3)

# 1~45범위 중복불가 나수 6개 생성
# np.unique(): 중복제거 함수
# x4 = np.unique(np.random.randint(1,46, size=6))
# print(x4)
#
# x5 = np.random.choice(45,6, replace=False) +1
# print(x5)

# # 배열 슬라이싱 하기 : [시작:끝:스텝]
# print('배열의 첫요소',e[0])
# print('배열의 첫요소',e[len(e)-1])
# print('배열의 첫요소',e[-1])

i = np.arange(10)    # 0~9 정수 배열
#
# print('처음부터 5번요소까지', i[:5])
# print('5번요소부터', i[4:])
# print('4~8', i[4:8])
# print('짝수', i[::2])
# print('2번부터 짝수요소마다', i[2::2])
# print('역순으로', i[::-1])
# print('5번부터 역순으로', i[5::-1])


j = np.array([[12,5,2,4],
             [7,6,8,8],
             [1,6,7,9]])

print('3*4배열',j)
#print('2행 3열',j[:2,:3])
# print('3행 2열',j[:3,:2])
# print('행기준 역순',j[::-1,:])
# print('열기준 역순',j[::,::-1])
# print('역순',j[::-1,::-1])
# print('2열',j[::,1])
print('2행',j[1,::])


# numpy로 생성한 배열중
# 1차원은 벡터 vector
# 2차원은 행렬 matrix
# 3차원은 텐서 tensor

# 배열을 부분적으로 slice 한 결과는
# 원본 배열의 복사본이 아니고 참조본임
# sql의 뷰와 유사한 개념
# 따라서, 참조본을 수정하면 원본에도 영향을 미침

k = np.array([1,2,3,4,5])
print('원본',k)

k_sub = k[1:3]
print('추출한 참조본',k_sub)

k_sub[0] = 100
k_sub[1] = 200
print('수정된 참조본',k_sub)
print('원본',k)


# 유니버셜 함수 - numpy 제공하는 범용 함수
l = np.array(range(1,10))

print('합',np.sum(l), l.sum())
print('표준편차',np.std(l))
print('평균',np.mean(l))
print('중앙값',np.median(l))
print('분산',np.var(l))
print('누적합',np.cumsum(l))

print('최대값',np.max(l))
print('최소',np.min(l))

print('곱',l*2)
print('제곱',l**2)
print('제곱근',np.sqrt(l))

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('열 합계',m.sum(axis=0))




# 배열객체 채우기
# 원소의 갑싱 없는 배열을 만들고
# 실행중에 각 원소에 값을 하나씩 채우는 방식
o = np.zeros((3,3))
print('원소가 0 인 3x3 행렬',o)

p = np.ones((5))
print('원소가 1 인 벡터',p)

q = np.arange(5)
print('원소가 0 부터 4까지인 1x5 벡터',q)



# boolean indexing
# 배열의 원소를 가리키기 위해 정수 인덱스를 사용했음
# 한편, bool값을 이용한 인덱싱도 가능
bool = [[True,False,True],
        [True, False, True],
        [True, False, True]]

ba = np.array(bool)
print('bool 값 인덱싱',m[ba])

# 구조화 배열 - 데이터베이스 테이블 생성과 유사
# 즉, 각 열마다 다른 자료형을 사용할 수 잇게 해줌
schema = np.dtype([('name','S10'),('age','i4'),('height','f')])
data = np.array([('smith',39,175.1),('darwin',10,120)],dtype=schema)
print('스키마가 정의된 배열',data)
print('이름만 출력',data['name'])
print('darwin의 나이 출력',data[1]['age'])

# 한글을 사용하고 싶다면
schema = np.dtype([('name','U10')])
data = np.array([('혜교'),('지현'),('수지')],dtype=schema)
print(data)


# 개인정보가 저장된 벡터를 이용해서
# 구조화 배열 생성
name = ['alice','bob','cathy','doug','hue']
age = [25,45,37,19,65]
weight = [55.5,85.2,61.3,61.5,110.9]

schema = {'names':('name','age','weight'),
          'formats': ('U10','i4','f4')}
personal = np.zeros(5, dtype=schema)
print(personal)

personal['name'] = name
personal['age'] = age
personal['weight'] = weight
print(personal)

print('1행만 출력',personal[0])
print('이름만 출력',personal['name'])
print('나이가 30보다 작은 사람만 출력',personal['age']<30)
print('나이가 30보다 작은 사람의 이름 출력',personal[personal['age']<30]['name'])




# 배열의 크기/구조 변형 - reshape
# 만들어진 배열의 데이터는 유지하면서 형태를 변경
origin = np.array([[1,1,1,1],
                   [2,2,2,2],
                   [3,3,3,3]])
print(origin)

# 3x4 -> 6x2 행렬
transform = origin.reshape(6,2)
print('6x2행렬\n',transform)

# 3x4 -> 2x6 행렬
transform = origin.reshape(2,6)
print('2x6행렬\n',transform)

# 3x4 -> 4x3 행렬
transform = origin.reshape(4,3)
print('4x3행렬\n',transform)

# 3x4 -> 12x1 행렬
transform = origin.reshape(12,1)
print('12x1행렬\n',transform)

# 3x4 -> 1x12 행렬
transform = origin.reshape(1,12)
print('1x12행렬\n',transform)

origin = np.arange(12)
# 1x12 => 3x4
transform = origin.reshape(3,4)
print('벡터 -> 행렬\n',transform)




# 밑에 두개는 둘다 안됨!
# # 1x12 => 3x5
# transform = origin.reshape(3,5)
# print('벡터 -> 행렬\n',transform)

# # 1x12 => 2x5
# transform = origin.reshape(2,5)
# print('벡터 -> 행렬\n',transform)

origin = np.arange(12)
# 차원수 -1로 사용하는 경우?
# 해당 행/열을 자동으로 계산해줌

transform = origin.reshape(3,4)
print('start\n',transform)

transform = origin.reshape(3,-1)
print('3,-1\n',transform)

transform = origin.reshape(4,-1)
print('4,-1\n',transform)

transform = origin.reshape(-1,4)
print('-1,4\n',transform)

transform = origin.reshape(-1,3)
print('-1,3\n',transform)


# 전치행렬
origin = np.arange(1,16)
transform = origin.reshape(3,5)
print(transform)

# 방법1
transform = origin.reshape(3,5).T
print(transform)

# 방법2
transform = np.transpose(origin.reshape(3,5))
print(transform)


# 두 배열 합치기 - broadcasting
# 일반적으로 두개의 행렬을 연한사는 경우
# 각 행렬의 크기는 서로 같아야 함
# 한편, numpy에서는 서로 다른 크기를 가진 행렬간 연산 가능
# 이때, 크기가 작은 행렬을 자동으로 확장(brodcast)해서
# 행렬의 크기를 맞춰 줌
# 파이썬의 리스트와 확연히 구분되는 기능

# 브로드캐스팅 연산 가능한 3가지 경우
# m*n & m*1
# m*n & 1*n
# m*1 & 1*n


a = np.array([[0,0,0],
              [10,10,10],
              [20,20,20],
              [30,30,30]])

b = np.array([[0,1,2],
              [0, 1, 2],
              [0, 1, 2],
              [0, 1, 2]])

c = np.array([0,1,2])
d = np.array([[0],
             [10],
             [20],
             [30]])

print(a)
print(b)
print(c)
print(d)

e = a+b
print(e)
f = a + c
print(f)
g = a + d
print(g)
h = c + d
print(h)

e = a+5
print(e)