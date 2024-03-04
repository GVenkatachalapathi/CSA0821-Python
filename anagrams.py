def group_anagrams(strs):
    anagram_groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    return list(anagram_groups.values())

# Take user input for the array of strings
user_input = input("Enter strings separated by spaces: ")
strs = user_input.split()

# Generate and print anagram groups
result = group_anagrams(strs)
print("Anagram Groups:", result)
