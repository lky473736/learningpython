r_r = o_p - p_p # 거스름돈
# 숙제 : 1000원 갯수 출력과 500원 갯수 출력까지!
r_1000 = r_r // 1000
r_change1 = r_r % 1000
r_500 = r_change1 // 500
r_change2 = r_change1 % 500
r_100 = r_change2 // 100
r_change3 = r_change2 % 100
r_10 = r_change3 // 10
r_change4 = r_change3 % 10

print ("거스름돈 : ", r_r)
print ("거스름돈을 이룰 수 있는 1000원의 갯수 : ", r_1000)
print ("거스름돈을 이룰 수 있는 500원의 갯수 : ", r_500)
print ("거스름돈을 이룰 수 있는 100원의 갯수 : ", r_100)
print ("거스름돈을 이룰 수 있는 10원의 갯수 : ", r_10)

