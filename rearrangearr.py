A = [1, 3, 4, 2, 0]
n = len(A)

for i in range(n):
    A[A[i] % n] += i * n

for i in range(n):
    A[i] //= n

print(A)