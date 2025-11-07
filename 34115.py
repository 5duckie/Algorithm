max_numbers_between = 0

N = int(input())
a = list(map(int,input().split()))
for n in range(1,N+1):
    idx1=-1
    idx2=-1
    for i in range(2*N):
        if a[i]==n:
            if idx1==-1:
                idx1 = i
            else:
                idx2 = i
    
    numbers_between = idx2-idx1
    if numbers_between > max_numbers_between:
        max_numbers_between = numbers_between
    
print(max_numbers_between)