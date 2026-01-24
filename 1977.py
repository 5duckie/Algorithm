min_val = 2000000000
total_sum = 0

m = int(input())
n = int(input())
for i in range(m,n+1):
    root = int(i**0.5)
    if root*root==i:
        total_sum+=i
        if min_val>i:
            min_val=i

if total_sum==0:
    print(-1)
else:
    print(total_sum)
    print(min_val)