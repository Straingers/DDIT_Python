arr = [0,0,0,0,0, 0,0,1,0,0]

for i, num in enumerate(arr):
    if num == max(arr):
        print(i)