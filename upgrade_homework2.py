# 과제 2. stack structure 구현
# 202334734 임규연 

import time # pop을 1초 간격으로 보여주기 위해서 time 모듈을 사용해 봄

slist = []
slist_history = [] # append한 각각의 리스트 상태를 이 리스트에 집어넣음

num = int(input("number of component at list? : ")) # 리스트 안 원소들 갯수 묻기

for i in range (num) :
    val = input("component : ")
    slist.append(val)
    slist_history.append(slist.copy()) # slist를 복사하여 추가해야 함
    print ("state : ", slist) # 현재 리스트 상태

print ("list history")
for j in range (len(slist_history)) :
    print (slist_history[j])
    
ready = int(input("start pop? If ready, press '0'. : "))

if ready == 0 :
    for k in range (len(slist)) :
        print (slist)
        slist.pop()
        time.sleep(1)
    