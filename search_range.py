def search_range(nums, target):
    def binary_search_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = binary_search_left(nums, target)
    right_index = binary_search_right(nums, target)

    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]

# Taking user input for the sorted array
user_input = input("Enter the sorted array separated by commas: ")
nums = list(map(int, user_input.split(',')))

# Taking user input for the target value
target = int(input("Enter the target value: "))

# Finding and displaying the starting and ending positions
result = search_range(nums, target)
print("Starting and ending positions:", result)
