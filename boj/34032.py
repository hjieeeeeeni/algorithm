n = int(input())
s = list(input())

half = n // 2

if n % 2 != 0:
    half += 1

if s.count("O") >= half:
    print("Yes")
else:
    print("No")