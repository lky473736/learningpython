# 튜플과 리스트의 차이점 : 튜플은 이미 정해진 값의 변경이 불가능. 하지만 값의 추가는 가능.
# 튜플 : ()
# 리스트 : []
# 딕셔너리 : {} (값을 두 가지 가짐. key와 value를 동시에 가지고 있음.)

stuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print (stuple)

# stuple[0] = 1
# 'tuple' object does not support item assignment

slist = list(stuple) # 튜플은 리스트로, 리스트는 튜플로 명시적 형변환 가능
print (slist)