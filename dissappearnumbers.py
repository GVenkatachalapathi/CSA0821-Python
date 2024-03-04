def dissappearnumbers(arr):
    n = len(arr)
    res = []
    all_nums = []
    for i in range(1,n+1):
        all_nums.append(i)
    for i in arr:
        if i in all_nums:
            all_nums.remove(i)
    return all_nums


n = int(input("enter size: "))
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)
print("Array :",arr)

result = dissappearnumbers(arr)
print("Result dissappearnumbers :",result)
