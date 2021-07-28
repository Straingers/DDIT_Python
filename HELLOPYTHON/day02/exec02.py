first = int(input("첫 숫자를 입력하시오 : "))
second = int(input("끝 숫자를 입력하시오 : "))

result = 0
for i in range(first, second + 1):
    result += i
print("모든 숫자의 합은 {}입니다".format(result))
