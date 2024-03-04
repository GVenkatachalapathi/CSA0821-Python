rows = int(input("enter no of rows :"))
cols = int(input("enter no of cols :"))

matrix = []

for i in range(rows):
    for j in range(cols):
        num = int(input())
        matrix.append(num)

print(matrix)
res = []
for i in range(rows):
    for j in range(cols):
        res.append(matrix[j])
        res.append(matrix[i])

print(res)

