list1 = ["서울", "인천", "부산"] # 리스트 만들기 (리스트는 colomn matrix로 나타냄)
list2 = [] # component가 없는 all-zero matrix

print("<list1>")
print("원본 : ", list1)
list1.append("천안") # 리스트 안에 component 집어넣기
print("천안을 넣은 결과 : ", list1)
list1.remove("인천")
print("인천을 뺀 결과 : ", list1)

print("<list2> ")
print("원본 : ", list2)
list2.append("도시")
print("도시를 넣은 결과 : ", list2)
list2.append("농촌")
print("농촌을 넣은 결과", list2)

# ~.sort : 내림차순 or 오름차순으로 수를 정렬 or 알파벳순 정렬 
