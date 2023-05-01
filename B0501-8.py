lists = [0, 10, 9, 2, 3, 6, 4, 2827, 3.14, 105, 326]
print (lists)

lists.sort() # 오름차순으로 정렬
print (lists)

lists.sort(reverse=True) # 내림차순으로 정렬
print (lists)

new_lists = sorted(lists) # sorted : 정렬된 list를 다른 변수에 대입하고 싶을 때 사용
print (new_lists)