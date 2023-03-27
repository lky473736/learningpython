# 임규연 (lky473736)
# AlphaMech_

# input (~) : 문자열을 인식 (string)
# 따라서 앞에 자료형을 첨부하여야 함 (int, float 등)

in_val = int(input("정수입력 : "))
fl_val = float(input("실수입력 : "))
st_val = input("입력 : ")

rst = fl_val / 3.3
print (str(fl_val) + "는" + str(rst) + "평입니다")
print ("입력 길이는 : ", str(len(fl_val))) # 출력하려면 str (문자열)로 변환해서 출력해야 한다
# len : 문자열의 길이를 의미 
# example : len ("가나다라마바사") = 7
