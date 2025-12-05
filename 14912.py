total = 0
n,d = map(int,input().split())
for i in range(1,n+1):
    a = str(i)
    for j in range(len(a)):
        if a[j]==str(d):
            total+=1

print(total)