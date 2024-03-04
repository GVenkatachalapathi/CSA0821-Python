def climb(n):
    if(n<=1):
        return 1
    else:
        return climb(n-1)+climb(n-2)
n=int(input("enter val :"))
print("Stairs ",climb(n))