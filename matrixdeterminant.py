matrix = []

print("Enter the elements of the 3x3 matrix row by row:")

for i in range(3):
    row = []
    for j in range(3):
        val = int(input(f"Enter element [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

a, b, c = matrix[0]
d, e, f = matrix[1]
g, h, i = matrix[2]

determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

print("\nYour Matrix:")
for row in matrix:
    print(row)

print(f"\nDeterminant: {determinant}")