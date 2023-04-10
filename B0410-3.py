import random

choice = random.choice (["왼", "중", "오"]) 
print ("왼, 중, 오 중에서 골라보세요!")
u_pass = input("입력 : ") # input 함수는 기본적으로 str을 입력받음


if (choice == u_pass) :
    print ("잘 막았네요")
    
else :
    print ("페널티킥 성공")