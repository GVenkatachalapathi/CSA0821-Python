num = int(input("Enter any number :"))
for i in range(1,num//2 + 1):
    if i ** 2 == num:
        print(i)
        break