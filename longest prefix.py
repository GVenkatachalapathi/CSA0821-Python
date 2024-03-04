def longestprefix(strings , n):
    if not strings:
        return ""
    
    strings.sort()
    print(strings)

    firststring = strings[0]
    laststring = strings[-1]

    commonprefix = []

    for i in range(len(firststring)):
        if i < len(laststring) and firststring[i] == laststring[i]:
            commonprefix.append(firststring[i])
        else:
            break
            
    return commonprefix

n = int(input("Enter no of strings :"))

strings = []
for i in range(n):
    str = input()
    strings.append(str)
print(strings)

result = longestprefix(strings,n)
print ("The Longest common prefix is ", result)


