a=[]
n1=int(input("Enter size :"))
for i in range(n1):
    elem=int(input())
    a.append(elem)
print(a)
b=[]
n2=int(input("Enter size :"))
for i in range(n2):
    ele=int(input())
    b.append(ele)
print(b)
c=[]
for i in a:
    c.append(i)
for i in b:
    c.append(i)
print(c)