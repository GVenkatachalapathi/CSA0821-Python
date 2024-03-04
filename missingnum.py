def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums_str = input("Enter distinct numbers separated by space: ")
nums = list(map(int, nums_str.split()))

result = missing_number(nums)
print(f"The missing number is: {result}")
