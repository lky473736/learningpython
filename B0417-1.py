# 임규연 (lky473736)

# 시험범위 : 함수까지 (다음 주 월요일에 시험)
# 화요일날 수업 X (화공강)
# 필기로 씀 (손코딩)

# function : 코드를 묶는 것 (def)
# object : 관련 있는 변수와 함수를 묶는 방법
# module : 함수나 객체들을 소스 파일 안에 모은 것 (라이브러리)

def print_address(name, ints) : # 매개변수 : name과 ints (2개)
    print ("성남시 수정구")
    print ("태평2동")
    print (name, ints)
        
    return ints + 1000 # 값 반환
    
# 변수 이름을 같은 것을 사용하는가? : 된다
# 원래 : 같은 변수명을 사용할 수 없음 (충돌이 일어날 수 있다)
# def 안 변수 = 지역변수
# def 밖 변수 = 전역변수
# 따라서, 지역변수와 전역변수는 동시에 사용이 가능하다. (똑같은 변수명을 사용할 수 있다)

name = input ("입력 : ")
rst = print_address(name, 1000)
print_address("result = ", rst)