# 화면 입출력
print("T", "E", "S", "T")  # T E S T

# sep="" :문자로 연결
print("T", "E", "S", "T", sep="")  # TEST
print("2024", "12", "20", sep="-")  # 2024-12-20

# end=" " 다음 프린트문과 연결/ 결과값: Life is too short You need Python
print("Life is too short", end=" ")
print("You need Python")

# 문자열 포매팅
# %d : 정수 ,%f : 부동소수,%c : 문자 1개,%s : 문자열
# %% : %라는 문자
# I eat 3 apples
apple = 3
print("I eat", apple, "apples")
print("I eat %d apples" % apple)

msg = "I eat %d apples" % apple
print(msg)

msg = "I eat %s apples" % apple
print(msg)

print("Error is %d%%" % 98)

number = 10
day = "three"
msg = "I eat %d apples, so I was sick for %s days" % (number, day)
print(msg)


# 포멧코드와 숫자 함께 사용
print("%s" % "hi")
print("%10s" % "hi")  # "hi"로 부터 전체 길이가 10이고 오른쪽 정렬, 나머지는 공백
print("%-10sjane" % "hi")  # "hi"로 부터 전체 길이가 10이고 왼쪽 정렬

# 소수점 n번째 자리까지 출력
# 0: 길이에 상관 하지 않음
# n.0 : 소수점 포함하연 n 자리를 사용하고 오른쪽 정렬 (-n.0 왼쪽 정렬)
print("%0.4f" % 3.141592152)
print("%10.4f" % 3.141592152)


# "".format()
msg = "I eat {} apples".format(apple)
print(msg)

msg = "I eat {} apples, so I was sick for {} days".format(number, day)
print(msg)

# f 문자열 포매팅


# 키보드 입력
# input()
# print("숫자 입력")
# msg = input()
# print(msg)

# msg = input("숫자 입력 : ")
# print(msg)

# 숫자 2개를 입력핟은 후 연산 프로그램 작성
# 입력받은 값 문자로 인식
num1 = int(input("첫번째 수 :"))
num2 = int(input("두번째 수 :"))
print(num1 + num2)
