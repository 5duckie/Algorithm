N = int(input())
a = []
for i in range(N):
    b = int(input())
    a.append(b)

b = []
for i in a:
    c = []
    for j in range(len(b)):
        if i>b[j]:
            c.append(b[j])
    b = c[:]
    b.append(i)
print(b)
print(len(b))