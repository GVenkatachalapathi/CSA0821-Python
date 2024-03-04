str=input("Enter a string :")
count=0
for i in range(len(str)):
    if(str[i]==" "):
        count=0
    else:
        count=count+1
print("length of last word :",count)