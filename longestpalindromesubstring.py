def longest_palindromic_substring(s):
    if not s:
        return ""

    n = len(s)
    start, max_length = 0, 1

    for i in range(n):
        # Check odd length palindromes
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # Check even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return s[start:start + max_length]

# Taking user input for the string
user_input = input("Enter a string: ")
result = longest_palindromic_substring(user_input)

# Displaying the result
print("Longest palindromic substring:", result)
