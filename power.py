def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n:
        if n % 2:
            result *= x
        x *= x
        n //= 2

    return result

# Take user input for the base and exponent
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

# Calculate and print the result
result = my_pow(x, n)
print("Result:", result)
