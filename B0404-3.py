year = int(input("연도를 입력하세요. : "))

condition = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

if (condition) :
    print (year, "는 윤년입니다.",)
    
else : 
    print ("평년입니다")