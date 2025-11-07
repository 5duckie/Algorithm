N = int(input())
a = []
for i in range(1,N+1):
    a.append(i)

while len(a)>1:
    a = a[1:len(a):2]

print(a[0])