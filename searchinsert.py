def search(a,target):
    for i in range(len(a)):
        if(a[i] >= target):
            return i
    return len(a)

a=[]
n = int(input("enter the number of elements :"))

for i in range(0,n):
    num=int(input())
    a.append(num)
print(a)
target = int(input("enter target :"))
result = search(a,target)
print("output :",result)