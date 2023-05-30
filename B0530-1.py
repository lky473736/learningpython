# 내장함수, 람다, 모듈, 상속
# 상속 : class를 활용한 객체 만들기 (오버로딩, 오버라이팅 중 오버라이팅이 상속임)
# 람다식 (lambda expression) : 소스코드의 축약
# 모듈 : random, turtle, tkinter, math, tensorflow ...
# 내장함수 : https://docs.python.org/ko/3/library/functions.html

# (ヽ   (ヽ
# ꒰〃´ ˆ `〃꒱
# (っ(함수)⊂)

# 절댓값 반환 : abs()

print (abs(-19132938129731987231))
print (abs(-1928.1234))

# sequence의 모든 component가 참일 때 True 반환 : all()
# 만약에 0이 하나라도 있다면 False (and 연산자)

slist = [1, 2, 3, 4]
print (all(slist)) # True

slist.append(0)
print (all(slist)) # False

# or 연산자 : any()

print (any(slist)) # True

# 수식 처리 및 계산 (입력받을 땐 str형이어야 함) : eval() 

formula1 = str(23 - 10 + 20 + 1)
print (eval(formula1))

formula2 = str(0 - 0) 
print (eval(formula2))

# 리스트에 존재하는 component 더하기 : sum()

'''alist = [[1, 2, 3], 10]
print (sum(alist[0] + 10)) # concatenate error
'''

alist = [i + 1 for i in range(10)]
print (sum(alist))

# 객체의 길이를 계산하기 : len()

print(len(alist))
print(len([[1, 2], 1, 2, 3])) # 4

# 리스트 생성 (글자, 요소별로 쪼개서 append): list()

s = 'abcdefg'
print (list(s))

t = (1, 2, 3, 4, 5)
print (list(t)) # tuple exchanges list

# 리스트나 튜플, 문자열에서의 최댓값, 최솟값 : max(), min()

k = 'abcdefghijklnmop'
print (max(k))

# 반복가능한 객체 (리스트, 튜플 등)의 각 항목에 주어진 함수를 적용한 후 결과 반환 (인수 2개 받음): map() 

def square (n) :
    return n ** 2

klist = [1, 2, 3, 4, 5]
result = list(map(square, klist)) # map (함수 이름, 반복가능한 객체)
print (result)

# sequence 객체를 입력받고 열거형 객체 반환 : enumerate()

elist = ['ok', 'pk', 'rk']
print (list(enumerate(elist))) # 반환될 때 각 component의 형태는 (index 번호, component 성분값)
print (list(enumerate(elist, start = 10))) # index의 시작 번호를 조정할 수 있음

# 특정 조건을 만족하는 요소만 뽑음 : filter()

def condition(x) :
    return x > 3

flist = [1, 2, 3, 4, 5]
print(list(filter(condition, flist))) # filter (함수 이름, sequence 이름)

# 정렬 : sort(), sorted()
# 1과 2는 같은 거임

# 1
glist = [1, 3, 0, 5, 2]
hlist = sorted(glist)
print (hlist)

# 2
glist = [1, 3, 0, 5, 2]
glist.sort()
print (glist)