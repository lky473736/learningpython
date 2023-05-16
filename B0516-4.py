infile = open ("/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/B0516-4.txt", "r")

# 공백을 기준으로 단어 단위로 분리하기
for line in infile :
    line = line.rstrip()
    wordlist = line.split()
    for word in wordlist :
        print (word)

infile.close()