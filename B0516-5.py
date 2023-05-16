infilename = input ("입력 파일 이름 입력 : ")
outfilename = input ("출력 파일 이름 입력 : ")
print ()

infile = open (infilename, "r")
outfile = open (outfilename, "w")

s = infile.read() # 입력 파일을 읽어서 s에 저장
outfile.write(s) # 그 s를 outfile에 복사

infile.close()
outfile.close()