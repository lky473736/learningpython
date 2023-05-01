lists = ['a', 'b', 'c', 'd']
print (lists)

lists.append ('k')
print (lists)

lists.remove ('k')
print (lists)

print (lists[0])

# 리스트 내 자료에 접근 : 리스트명[자리수]
# lists = ['a', 'b', 'c', 'd']
#           0    1    2    3

for i in lists : # 리스트 안에서의 반복문. 여기서 i는 lists[i]랑 동일한 말이 된다.
    print (i, end = " ") # end = " " : 큰따옴표 안에 있는게 출력하는 끝머리에 붙음
    
print (" ")