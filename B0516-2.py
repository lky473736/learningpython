infile = open ("/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/B0516-2.txt", "r")
# open ("경로", mode) : mode에 따라 파일 여는 매소드 
# 파일 데이터 읽기 순서 : 파일 열기 -> 파일에서 데이터를 읽거나 씀 -> 파일 닫기

# mode : r (read) , w (write) , a (append)

# 1
line1 = infile.read() # 파일을 한번에 읽는 매소드 
print (line1)

'''<참고> 
line2 = infile.readlines() # 파일을 리스트 형태로 한줄씩 읽는 매소드
print (line2)'''

# 2
for line1 in infile : 
    line = line.rstrip() # 개행 문자를 잘라냄 
    print (line)

infile.close() # 파일 닫는 매소드

# 1이랑 2랑 똑같음
# https://velog.io/@code_angler/Python-%EB%AC%B8%EC%9E%90-%EC%A0%9C%EA%B1%B0-by.-String-striprstriplstrip-%EC%82%AC%EC%9A%A9
