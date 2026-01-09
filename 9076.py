T = int(input())
a = []
for i in range(T):
    N = list(map(int,input().split()))
    a.append(N)
    a.sort()

print(a)