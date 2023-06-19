# 주어진 LOTTO 프로그램 코드 해석 및 나의 방식대로 LOTTO 프로그램 구현하기

# 먼저 주어진 'lotto.py'의 코드는 아래와 같은 방식으로 진행됨.
# 1) counters는 45개의 원소로 이루어져 있고 전부 0으로 초기화되어 있음.
# 2) no()는 주어진 횟수(r_in)만큼 번호를 선택하고, 선택된 번호들의 횟수를 counters 리스트에 반영함.
# 3) one(), two(), three(), four()는 각각 1개, 2개, 3개, 4개의 번호를 제외하고 선택하는 경우임.
# 4) in_call()는 사용자에게 "몇 번 수행할까요?"라고 묻고, 사용자가 입력한 값을 정수로 변환하여 반환함.
# 5) c_y 변수에 미리 확정한 숫자의 개수를 입력받고, c_y에 따라 경우가 나뉘어짐.
# 5-1) c_y == 4 : 사용자로부터 4개의 숫자(in_v, in_w, in_x, in_y)를 입력받고, in_call() 후 four()
# 5-2) c_y == 3 : 사용자로부터 3개의 숫자(in_v, in_w, in_x)를 입력받고, in_call() 후 three()
# 5-3) c_y == 2 : 사용자로부터 2개의 숫자(in_v, in_w)를 입력받고, in_call() 후 two()
# 5-4) c_y == 1 : 사용자로부터 1개의 숫자(in_v)를 입력받고, in_call() 후 one()
# 5-5) c_y == 0 : in_call() 후 no()
# 그동안 파이썬 강좌에서 배운 def, 내장 함수 등을 사용하여 LOTTO 프로그램을 구현하였다.

# 임규연의 LOTTO 프로그램 : 
# 1) 먼저 자신이 구매할 복권 갯수를 물음 -> 각 복권에 넣을 수 6개를 입력받음
# 2) random으로 금주의 복권 결과를 출력하고 자신이 입력한 각 복권의 수와 대조하여 당첨되었는지를 출력

import random

lottolist = [] # 로또 번호 6개 넣을 리스트 (복권 하나당 한 component, 6개의 번호가 한 list를 이룸)
# 예시 : [[2, 5, 32, 24, 1, 4], [3, 2, 6, 43, 24, 33]] : 복권 2개, 각 복권의 component

winner_numlist = [] # 금주의 로또 번호

bonusnum = 0 # 보너스 숫자 변수 선언

while True : 
    if len(winner_numlist) == 6 :
        break 
    
    p = random.randint (1, 45)
    
    if p not in winner_numlist :
        winner_numlist.append(p)
        
    else :
        pass

lottonum = int(input("몇 개의 복권을 구매하실 겁니까? : ")) 

for i in range (lottonum) :
    lottolist.append ([]) # 복권 갯수만큼 리스트 component 생성

for i in range (lottonum) :
    print ("%d번째 복권의 숫자 6개를 입력합니다." %(i + 1))
    for j in range (6) : 
        print (lottolist[i])
        component = int(input("%d번째 숫자 입력 : " %(j + 1)))
        
        if component <= 45 and component > 0 : # 복권 숫자가 1~45 이면
            if component not in lottolist : # 복권 숫자가 중복되지 않았으면
                lottolist[i].append (component) # 리스트에 append
                
            else : # 복권 숫자가 중복되었으면
                print ("중복된 숫자를 입력하셨습니다. 시스템을 종료합니다.")
                exit()
                
        else : # 복권 숫자가 1~45가 아니면
            print ("범위에 맞지 않는 숫자를 입력하셨습니다. 시스템을 종료합니다.")
            exit()
            
print ("금주의 로또 번호는 : ", winner_numlist)
print (list(enumerate(lottolist, start = 1)))

while True : # 보너스 숫자   
    if bonusnum not in winner_numlist and bonusnum != 0 : # 초기 선언한 값이 아니면서 
        break
    
    bonusnum = random.randint (1, 45)

print ("보너스 번호는 : ", bonusnum)

for u in range (len(lottolist)) : # 교집합의 component의 갯수로 복권 등수를 결정
    if sorted(lottolist[u]) == sorted(winner_numlist) : 
        print (lottolist[u], " : 로또 1등 당첨! (숫자 6개)")
    
    elif len(set(lottolist[u]) & set(winner_numlist)) == 5 and bonusnum in lottolist[u] :
        print (lottolist[u], " : 로또 2등 당첨! (숫자 5개 + 보너스 숫자)")
        
    elif len(set(lottolist[u]) & set(winner_numlist)) == 5 :
        print (lottolist[u], " : 로또 3등 당첨! (숫자 5개)")
        
    elif len(set(lottolist[u]) & set(winner_numlist)) == 4 :
        print (lottolist[u], " : 로또 4등 당첨! (숫자 4개)")
        
    elif len(set(lottolist[u]) & set(winner_numlist)) == 3 :
        print (lottolist[u], " : 로또 5등 당첨! (숫자 3개)")
    
    else :
        print (lottolist[u], "는 꽝! 복권에 당첨되지 않았습니다.")
    


''' 원본 코드 ('lotto.py')

import random
counters = [0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0
            ,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0]

#in_val1 = 46
#in_val2 = 46

print("간단하게 수행되는 LOTTO 프로그램 ")
print()
in_val = []


def no(r_in):
    for i in range(r_in):            
        value = random.randint(0, 44)
        counters[value] = counters[value] + 1
         
    for i in range(45):
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)
    print("---------------------------------------------------------")
    for i in range(7): 
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0
            

def one(r_in, in_val0):
    for i in range(r_in):
        value = random.randint(0, 44)
        if value == in_val0:  #in_val1
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1

    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)
    print("---------------------------------------------------------")
    for i in range(7) : 
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0
  

def two(r_in, in_v0, in_v1):
    for i in range(r_in):
        value = random.randint(0, 44)

        if value == in_v0:  #in_val1
            counters[value] = 0
        elif value == in_v1:   #in_val2
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1
        #counters[value] = counters[value] + 1
     
    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)
    print("---------------------------------------------------------")
    for i in range(7) : 
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0
  
            

def three(r_in, in_v, in_w, in_x):
    for i in range(r_in): # 몇번을 돌릴것인지 결정
        value = random.randint(0, 44)

        if value == in_v:  #in_val1
            counters[value] = 0
        elif value == in_w:   #in_val2
            counters[value] = 0
        elif value == in_x:    #in_val3
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1
    
    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)
    print("---------------------------------------------------------")
    for i in range(7) : 
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0
  
 
        
def four(r_in, in_v, in_w, in_x, in_y):
    for i in range(r_in): # 몇번을 돌릴것인지 결정
        value = random.randint(0, 44)

        if value == in_v:  #in_val1
            counters[value] = 0
        elif value == in_w:   #in_val2
            counters[value] = 0
        elif value == in_x:    #in_val3
            counters[value] = 0
        elif value == in_y:    #in_val4
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1
    
    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)
    print("---------------------------------------------------------")
    for i in range(7) : 
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0
  
 
def in_call():
    rot = int(input("몇번 수행할까요? : "))
    return rot


c_y = int(input("미리 확정한 숫자가 몇개 있습니까? (0 ~ 4개) "))


for i in range(5):
    

    if (c_y == 4):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
            in_w = int(input(" 숫자 입력 : ")) -1
            in_x = int(input(" 숫자 입력 : ")) -1
            in_y = int(input(" 숫자 입력 : ")) -1
            in_val.append(in_v)
            r_in = in_call()
            four(r_in, in_v, in_w, in_x, in_y)
    elif (c_y == 3):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
            in_w = int(input(" 숫자 입력 : ")) -1
            in_x = int(input(" 숫자 입력 : ")) -1
            in_val.append(in_v)
            r_in = in_call()
            three(r_in, in_v, in_w, in_x)
    elif (c_y == 2):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
            in_w = int(input(" 숫자 입력 : ")) -1
            in_val.append(in_v)
            r_in = in_call()
            two(r_in, in_v, in_w)
    elif (c_y == 1):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
   #         in_val.append(in_v)
            r_in = in_call()
            print(in_val)
            one(r_in, in_v )
    elif (c_y == 0): 
        rst = in_call()
        no(rst)
    else:
        print("다시 선택해 주세요!")'''
