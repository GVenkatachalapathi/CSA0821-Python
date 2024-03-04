a = []

n = int(input("enter no of elements :"))

for i in range(0,n):
    num=int(input())
    a.append(num)
print(a)

if(a[n-1] == 9):
    a[n-2] = a[n-2] + 1
    a[n-1] = 0
else:
    a[n-1] = a[n-1] + 1

print("output :",a)
