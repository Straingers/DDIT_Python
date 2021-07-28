import random

mine = input("홀/짝을 선택하세요\n")
# a = random.randrange(1, 100)
#
# print("생성된 난수 : " + str(a))
#
# if a % 2 == 0 and mine == "짝":
#     print("성공!")
# elif a % 2 == 1 and mine == "홀":
#     print("성공!")
# else:
#     print("실패!")
com = random.choice("홀짝")
print("컴퓨터 :", com)
if mine == com:
    print("성공")
else :
    print("실패")
