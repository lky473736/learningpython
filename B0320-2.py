# 별까지의 거리 계산하기

# dist = 40000000 # 실체 거리 : 상수 : 거리니깐 변할 수 있다
speed = 300000 # 실체 속도 : 상수 : 불변

dist = int(input("거리 : ")) # dist라는 변수에 정수형의 값을 입력받는다 -> 입력받은 값은 변수에 저장한다
r_dist = dist / speed
si = r_dist // 3600 # 60*60
bun = (r_dist - (si*3600)) // 60
cho = r_dist%60 # 나머지 (modular)
print (r_dist, "은", bun, "분", cho, "초")
print (r_dist, "은", si, "시", bun, "분", cho, "초")