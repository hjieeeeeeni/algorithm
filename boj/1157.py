w = input().upper()
list = list(set(w))

cnt = []

for i in list:
    cnt.append(w.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(list[cnt.index(max(cnt))])