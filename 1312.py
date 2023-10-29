A, B, N = map(int, input().split())
print(A/B)
A %= B
print(A)
for i in range(N - 1):
    A = (A * 10) % B
    print(A)

print((A * 10) // B)
