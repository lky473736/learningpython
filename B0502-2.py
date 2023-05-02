scorelist = []
cnt = 0

number = int(input("학생들 수를 입력 : "))

for i in range (number) :
    score = float(input("점수 입력 : "))
    scorelist.append (score)
        
    if score >= 80 :
        cnt = cnt + 1

print ("성적 평균 : ", sum(scorelist) / len(scorelist))
print ("최대 점수 : ", max(scorelist))
print ("최소 점수 : ", min(scorelist))

print ("80점 이상 갯수 : ", cnt)