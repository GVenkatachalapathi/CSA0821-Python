n1=int(input("Enter first binary number :"))
decimal=0
base=1
while(n1!=0):
	rem=n1%10
	decimal=decimal+rem*base
	n1=n1//10
	base=base*2
print(decimal)
n2=int(input("Enter first binary number :"))
decimal1=0
base1=1
while(n2!=0):
	rem=n2%10
	decimal1=decimal1+rem*base1
	n2=n2//10
	base1=base1*2
print(decimal1)
sum=decimal+decimal1
print("sum :%d"%sum)
arr=[]
binary=0
while(sum!=0):
	arr.append(sum%2)
	sum=sum//2
arr.reverse()
for i in arr:
	binary=binary*10+i
print("Binary :",binary)