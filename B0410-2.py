# 임규연 (lky473736)
# 회원가입 및 로그인 시스템

print ("회원가입을 진행합니다.")
id = input ("아이디를 입력해주세요. : ")
pw = input ("비밀번호를 입력해주세요. : ")

print ("회원가입이 완료되었습니다.")
inid = input ("아이디를 입력해주세요. : ")

if inid == id :
    inpw = input ("비밀번호를 입력해주세요. : ")
    if inpw == pw :
        print ("일치합니다.")
        
    elif inpw != pw : 
        print ("비밀번호가 일치하지 않습니다.")
        
    else :
        print ("오류가 발생하였습니다. 프로그램을 종료합니다.")
        quit
        
else :
    print ("아이디가 일치하지 않습니다. 프로그램을 종료합니다.")
    quit