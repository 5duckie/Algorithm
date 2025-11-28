a = []

for i in range(8):
    b = int(input())
    a.append(b)

b = []
b = a[:]
notch = []
a = sorted(a)
for i in range(5):
    notch.append(b.index(a[-i-1])+1)

print(sum(a[-1:-6:-1]))
print(*sorted(notch))