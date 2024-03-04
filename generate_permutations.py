def generate_permutations(nums):
    def helper(index):
        if index == len(nums) - 1:
            result.append(nums.copy())
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            helper(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    result = []
    helper(0)
    return result

# Take user input for the array
user_input = input("Enter distinct integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Generate and print permutations
result = generate_permutations(nums)
print("Permutations:", result)
