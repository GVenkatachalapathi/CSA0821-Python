def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Exact match found

    return closest_sum

# Taking user input for the integer array
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

# Taking user input for the target
target = int(input("Enter the target: "))

# Finding and displaying the closest sum
result = three_sum_closest(arr, target)
print("Closest sum to target:", result)
