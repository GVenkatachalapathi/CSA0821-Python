def length_of_longest_substring(s):
    char_set = set()   # Create an empty set to store unique characters
    max_length = 0     # Initialize the maximum length of substring without repeating characters
    start = 0          # Initialize the starting index of the current substring

    for end in range(len(s)):  # Loop through the characters of the input string
        while s[end] in char_set:  # While the current character is already in the set
            char_set.remove(s[start])  # Remove the character at the starting index from the set
            start += 1  # Move the starting index to the right

        char_set.add(s[end])  # Add the current character to the set
        max_length = max(max_length, end - start + 1)  # Update the maximum length of substring

    return max_length  # Return the final maximum length

# Taking user input for the string
user_input = input("Enter a string: ")
result = length_of_longest_substring(user_input)

# Displaying the result
print("Length of the longest substring without repeating characters:", result)

