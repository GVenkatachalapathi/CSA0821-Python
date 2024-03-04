n = int(input("Enter number :"))
a = 0
b = 1

print(a,b)
sum = 0
for i in range(2,n):

    c = a + b
    sum = sum + c
    print(c,end=" ")
    a = b
    b = c
print("\nsum :",sum+1)
