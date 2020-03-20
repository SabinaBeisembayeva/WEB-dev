a = int(input())
arr = []
for i in range(a):
    x = int(input())
    arr.append(x)
for i in range(1,len(arr)):
    if arr[i] == arr[i - 1]:
        print("YES")
        break
    else:
        print("NO")
        break