def lengthoflastword(str):
    words = str.split()
    if words:
        print(words)
        return len(words[-1])
    else:
        return 0
    
str = input("Enter any string :")

result = lengthoflastword(str)
print("length of last word is",result)


