import random

mine = input("가위/바위/보\n")
result = ""

rand = random.random()

if rand < 0.33:
    com = "가위"
elif rand < 0.66:
    com = "바위"
else:
    com = "보"

if mine == "가위" and com == "보":
    result = "이김"
elif mine == "바위" and com == "가위":
    result = "이김"
elif mine == "보" and com == "바위":
    result = "이김"
elif mine == "가위" and com == "바위":
    result = "짐"
elif mine == "바위" and com == "보":
    result = "짐"
elif mine == "보" and com == "가위":
    result = "짐"
else:
    result = "비김"

print("mine:", mine)
print("com:", com)
print("result", result)