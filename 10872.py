N = int(input())
def stori(n):
    if n==0:
        return 1
    return n*stori(n-1)
print(stori(N))