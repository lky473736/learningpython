fl_val1 = float(input("몸무게 입력 : "))
fl_val2 = float(input("키 입력 : "))

bmi = fl_val1 / (fl_val2 ** 2)

print ("당신의 bmi는 " + str(bmi) + "입니다")

if bmi < 18.5 : 
    print ("당신은 저체중입니다")

elif 18.5 < bmi < 30 :
    print ("당신은 표준입니다")
    
elif bmi > 30 : 
    print ("당신은 비만입니다")

