pbook = {}

pbook["홍길동"] = "010-1234-5678" # 홍길동이라는 key 생성, 거기에 value 입력

print (pbook["홍길동"]) # key를 이용한 value 검색

pbook["강감찬"] = "010-9876-5432"

print (pbook["강감찬"])

pbook["광개토대왕"] = "010-1928-3746"

print (pbook["광개토대왕"])

for i in pbook :
    print (i, pbook[i])
    
sear = input("검색 시스템 : key를 입력하세요. : ")
print (pbook[sear])