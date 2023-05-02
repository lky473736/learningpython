import random

numbers = [10, 20, 30, 40, 50]
lista = ["ok", "rk", "pk", "nk"]

print ("랜덤 값 (in numbers) : ", random.choice(numbers))
print ("랜덤 값 (in lista) : ", random.choice(lista))

print ("합 = ", sum(numbers))
print ("최댓값 = ", max(numbers))
print ("최솟값 = ", min(numbers))