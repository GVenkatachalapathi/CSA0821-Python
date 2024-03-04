def generate_pascals_triangle(numRows):
    triangle = []
    
    for i in range(numRows):
        row = [1] * (i + 1)
        
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle

# User Input
numRows = int(input("Enter the number of rows for Pascal's triangle: "))

# Output
result = generate_pascals_triangle(numRows)
print(f"Pascal's triangle with {numRows} rows: {result}")
