a = []
temp = 0
n = int(input("Enter size: "))
for i in range(0, n):
    ele = int(input("Enter element: "))
    a.append(ele)
print("Original list:", a)
for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
print("Sorted list:")
for i in a:
    print(i)