def valid_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return s[i+1:] == s[i+1:][::-1] or s[i:len(s)-1-i] == s[i:len(s)-1-i][::-1]
    return True

# Get user input for the string
s = input("Enter a string: ")

# Display the result
print(f"The string can be a palindrome after deleting at most one character: {valid_palindrome(s)}")
