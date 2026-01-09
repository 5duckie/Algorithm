T = int(input())
for i in range(T):
    N = int(input())
    b = N**2
    b = str(b)
    N = str(N)

    if b[-len(N):]==N:
        print("YES")
    else:
        print("NO")