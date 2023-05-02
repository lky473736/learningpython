# list concatnation, comparison, copy 
# https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%9E%90%EC%97%B4_%EC%97%B0%EA%B2%B0

lista = [1, 2, 3, 4, 5]
listb = [5, 6, 7, 8, 9]

listc = lista + listb # 중복이 되어도 중복된 거 그대로 표시 (합집합표현이랑 다름)

print ("-concatnation-")
print ('lista :', lista)
print ('listb :', listb)
print ('concatnation :', listc)
print ()

print ("-comparison-")
print ('lista * 5 =', lista * 5)
print (lista == listb) # 리스트 비교
print (lista != listb)
print (lista > listb) # 리스트에서 대소 : sum? 아니면 전체적인 평균?
print ()

# 복사의 종류 : 얕은 복사, 깊은 복사

print ("-thin copy-")
print ("original lista :", lista)
c_lista = lista # 리스트 전체를 복제
print ('copy lista thinly :', c_lista)
c_lista[0] = 'p'
c_lista[1] = 'k'
print ("thin copy of 'p', 'k' at position '0', '1' : ", c_lista) # 한 요소를 바꿈
print ()

print ("-deep copy-")
print ('original listb :', listb)
c_listb = list(listb) # 리스트 전체를 복제해서 다른 리스트를 새로히 만들어서 안에 요소로 넣음
print ('copy listb deeply :', c_listb)
c_listb[0] = 1
print (c_listb)