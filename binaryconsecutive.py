def consecutiveones(bin_arr):
    count = 0
    res = 0
    for i in bin_arr:
        if i == 1:
            count = count + 1
            res = max(res, count)
        elif i == 0:
            count = 0
    return res

n = int(input(f"Enter a size: "))
bin_arr= []

for i in range(n):
    bin_arr.append(int(input()))
print(bin_arr)
result = consecutiveones(bin_arr)
print("output :",result)
