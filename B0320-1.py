# 임규연 (lky473736)

# 변수의 세부 구현 사항 : 객체의 참조값(주소)
# 파이썬 : 객체 지향 언어 -> 변수나 클래스 등을 객체로 취급
# interpreter : id (변수) : 변수에 대한 객체아이디 출력 (컴퓨터에 따라 다르다)

x = int(input())
print (id(3))
print (id(x), "-->", x)

# 변수를 얉은복사할때 : 참조값의 복사
# 변수1 = 변수2 사용

# 변수를 깊은복사할때 : ?

# 불변객체 : 상수, 문자열, 튜플 (한번 만들어지면 변경 불가)
# 가변객체 : 변수, 리스트, 세트, 딕셔너리 (언제나 변경 가능한 객체)

