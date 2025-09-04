n, m = map(int, input().split())

packege = []
single = []

for _ in range(m):
    a, b = map(int, input().split())
    packege.append(a)
    single.append(b)

x = min(packege)
y = min(single)

result = min(n//6 * x + n % 6 * y, (n//6 + 1) * x, n * y)

print(result)