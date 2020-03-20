a = int(input())
arr = []
summa = 0
for i in range(a):
    x = int(input())
    arr.append(x)
for i in arr:
    if i >= 0:
        summa = summa + 1
print(summa)