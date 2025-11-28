N = int(input())
a = []
for i in range(N):
    b = int(input())
    a.append(b)

print(*sorted(a),sep='\n')