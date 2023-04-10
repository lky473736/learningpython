# 임규연 (lky473736)

'''
time = int(input("지금 시간은 몇시입니까? : "))
weather = input("지금의 날씨는 어떱니까?")

if 6 < time < 9 and weather == "화창하다" :
    print ("종달새가 노래합니다.")
'''
    
import random 

time = random.randint(1, 24)
# https://blockdmask.tistory.com/383
weather = random.choice([True, False]) 
# random.choice : 컴퓨터가 랜덤되게 괄호 안에 있는 값을 선택할 수 있게 함
# random.randint : 컴퓨터가 랜덤되게 괄호 범위 안에 있는 값을 무작위로 선택할 수 있게 함

print (time, weather)

if time >= 6 and time < 9 and weather == True : 
    print ("울어요")
    
else :
    print ("안울어요")