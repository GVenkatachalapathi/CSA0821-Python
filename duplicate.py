a=[]
b=[]
n=int(input("Enter Size :"))
for i in range(n):
    ele=int(input())
    a.append(ele)
print(a)
for i in a:
    if i not in b:
        b.append(i)
print(b)
