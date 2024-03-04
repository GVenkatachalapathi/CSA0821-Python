def find_max_average(nums, k):
    n = len(nums)
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum = current_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k

nums = list(map(int, input("Enter the array elements separated by space: ").split()))
k = int(input("Enter the value of k: "))

result = find_max_average(nums, k)
print(f"The maximum average of a subarray of length {k} is: {result:.5f}")
