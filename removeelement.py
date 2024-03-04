a=[]
n=int(input("Enter size :"))
for i in range(n):
    ele=int(input())
    a.append(ele)
a.sort()
print(a)
num=int(input("Enter num to remove :"))
for i in a:
        a.remove(num)
print(a)