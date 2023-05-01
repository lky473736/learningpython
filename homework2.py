''' stack structure : a echelon form for datas

1) append를 사용하여 계단 형태로 데이터를 표현
2) pop을 이용하여 stack의 구조 확인

참고 : https://www.programiz.com/dsa/stack
'''

lists = [0, 1, 2, 3, 4]
print(lists)

lists.append(10)
print(lists)

lists.append(11)
print(lists)

lists.pop()
print(lists)

lists.pop()
print(lists)

lists.pop()
print(lists)
