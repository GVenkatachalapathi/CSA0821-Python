n=int(input("Enter any number :"))
temp=n
reverse=0
while(n>=0):
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
print(reverse)
if(reverse==temp):
    print("Palindrome")
else:
    print("Not a palindrome")
