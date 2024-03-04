def find_single_number(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

nums_str = input("Enter the array of integers separated by space: ")
nums = list(map(int, nums_str.split()))

# Output
result = find_single_number(nums)
print(f"The single number in the array is: {result}")
