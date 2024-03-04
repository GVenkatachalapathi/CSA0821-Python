def multiply_strings(num1, num2):
    result = 0

    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')
            result += (digit1 * 10**(len(num1)-1-i)) * (digit2 * 10**(len(num2)-1-j))

    return str(result)

# Take user input for the two numbers represented as strings
num1 = input("Enter the first number as a string: ")
num2 = input("Enter the second number as a string: ")

# Calculate and print the product
result = multiply_strings(num1, num2)
print("Product:", result)
