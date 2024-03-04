n = int(input("Enter  the number :"))
binarynumber = bin(n)[2:]
print(binarynumber)
complement = ""
for bit in  binarynumber:
    if bit == '0':
        complement += '1'
    elif bit == '1':
        complement += '0'
print(complement)
convert = int(complement)
print(convert)

decimal=0
base=1
while(convert!=0):
	rem=convert%10
	decimal=decimal+rem*base
	convert=convert//10
	base=base*2
print(decimal)