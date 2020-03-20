a = int(input())
arr = []
summa = 0
for i in range(a):
    arr.append(int(input()))
for i in range(1, len(arr)):
    if arr[i]>arr[i-1]:
        summa+=1
print(summa)