def max_subarray_sum(nums):
    max_sum = 0
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Take user input for the array of integers
user_input = input("Enter integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Find and print the maximum subarray sum
result = max_subarray_sum(nums)
print("Maximum Subarray Sum:", result)
