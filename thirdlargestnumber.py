def thirdmaxnumber(arr):
    if len(arr) < 3:
        print("largest num :",max(arr))
    else:
        print("3 largest num ",arr[2])


n = int(input("Enter size :"))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
print(arr)
arr.sort(reverse=True)
print(arr)
thirdmaxnumber(arr)

