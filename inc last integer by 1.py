a=[]
n=int(input("Enter size :"))
for i in range(n):
    ele=int(input())
    a.append(ele)
print(a)
a[n-1]=a[n-1]+1
print(a)