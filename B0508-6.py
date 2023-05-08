scoredic = {"kim" : [99, 83, 95],
            "lee" : [68, 45, 78],
            "choi" : [25, 56, 69]}

for a, b in scoredic.items() : # 매개변수 2개를 이용한 반복문 (in item 필요)
    print (a, b)
    
for i in scoredic :
    print (i, "의 평균성적 = ", sum(scoredic[i]) / len(scoredic[i]))