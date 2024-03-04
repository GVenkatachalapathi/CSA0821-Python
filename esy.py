a=[]
n=int(input("Enter data :"))
for i in range(n):
    element=int(input())
    a.append(element)
print(a)
target=int(input("Enter Target value :"))
for i in a:
    for j in a:
        if(i+j==target):
            print(a.index(i),a.index(j))
    