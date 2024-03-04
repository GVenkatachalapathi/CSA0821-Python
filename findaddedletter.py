def findaddedletter(str1,str2):
    res = []
    for char in str2:
        if char not in str1:
            res.append(char)
    return res



str1 = input("Enter First string :")
str2 = input("Enter Second string :")

result = findaddedletter(str1,str2)
print(result)
