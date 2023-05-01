lists = ['p', 'q', 'r']
print (lists)

lists[1] = 'x' # 1번 자리에 q 대신 x로 변경
print (lists)

lists.insert (1, 'y') 
# lists.insert (a, b) : a번 자리에 b 넣고 뒤의 나머지 자료들을 한 자리수 밀려나게 함
print (lists)

lists.pop() # stack에서 맨 끝자리 수 지움
print (lists)

# 과제 : stack 구조 만들기 