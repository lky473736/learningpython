# 참고 : https://wikidocs.net/63

def calculate_area (rad) :
    area = 3.14 * pow (rad, 2)
    return area # return은 함수 f(x)의 y값도 같은 것.

val = float(input("rad 입력 : "))
completed_area = calculate_area(val) 
# 함수에 val을 넣어서 return된 값을 completed_area 변수에 넣는다
print(completed_area)