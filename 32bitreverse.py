def reversenum(num):

    min = -2**31
    max = 2**31 - 1
    sign = -1 if num<0 else 1
    num *= sign

    reminder = 0
    reversed = 0
    while num != 0:
       reminder = num % 10
       reversed = reversed * 10 +reminder
       num //= 10

    return reversed * sign
 

num = int(input("Enter a number: "))

result = reversenum(num)
print ("Reversed Number is : ", result)
