def hammingdistance(n,x,y):
    
    all = []
    count = n
    for i in range(1,n+1):
        all.append(i)
    if x in all:
        count = count - 1
    if y in all:
        count = count - 1
    return count

x = int(input("Enter x distance :"))
y = int(input("Enter y distance :"))

if x > y:
    n = x
else:
    n = y
result = hammingdistance(n,x,y)
print(result)  



