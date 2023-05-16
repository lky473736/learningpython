outfile = open("/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/B0516-3.txt", "w", encoding = "UTF-8")
# 인코딩을 선언하지 않으면 깨질 수 있음. 인코딩을 이용해서 포맷을 선언하기.
# 파일이 없으면 자기가 알아서 새로 생성해줌

for i in range (100) :
    i = str(i) # .write는 항상 str로 써줘야 함
    outfile.write (i)
    outfile.write ("\n")
    
outfile.close()