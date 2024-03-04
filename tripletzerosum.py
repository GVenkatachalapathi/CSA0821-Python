def tripletzerosum(arr):

    arr.sort()
    res = []
    
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1


        while left < right:

            currentsum = arr[i] + arr[left] + arr[right]

            if currentsum < 0:
                left = left + 1
            elif currentsum > 0:
                right = right - 1
            else:
                res.append([arr[i] , arr[left] , arr[right]])
                left = left + 1
                right = right - 1

    return res

n = int(input("Enter no of elements :"))

arr = []

for i in range(n):
    arr.append(int(input()))

result = tripletzerosum(arr)
print("out put ",result)
