a = int(input())
arr = []
summa = 0
for i in range(a):
    x = int(input())
    arr.append(x)
for i in range(1 , len(arr)-1):
    if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
        summa+=1
print(summa)