haystack = input("enter the haystack string: ")
needle = input("enter the needle string: ")

index = -1
for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i + len(needle)] == needle:
        index = i
        break

print("Output:", index)