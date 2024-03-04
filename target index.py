a=[]
count=0
n=int(input("enter no.of input:"))
for i in range(0,n):
    num=int(input())
    a.append(num)
print(a)
digit=int(input("enter the target"))
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i] + a[j] == digit):
            print(i,j)
            count=count+1
if(count==0):
    print("no elements found")