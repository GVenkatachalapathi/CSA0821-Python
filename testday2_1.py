def maxavgvalue(nums,k):
    n = len(nums)
    currentsum = sum(nums[:k])
    maxsum = currentsum

    for i in range(k,n):
        currentsum = currentsum + nums[i] - nums[i-k]
        maxsum = max(currentsum,maxsum)
    return maxsum/k

n = int(input("Enter size :"))

nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

print(nums)

k = int(input("Enter K value :"))

result = maxavgvalue(nums,k)
print(result)
