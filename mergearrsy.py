a=[]
b=[]
c=[]
n = int(input("enter no of elements in first array :"))
m = int(input("enter number of elements in second array :"))
for i in range(0,n):
    num = int(input())
    a.append(num)
print(a)
for i in range(0,n):
    num = int(input())
    b.append(num)
print(b)
for i in range(0,n+m):
    if(i<n):
        c.append(a[i])
    else:
        c.append(b[i-n])
print(c)
print(sorted(c))
