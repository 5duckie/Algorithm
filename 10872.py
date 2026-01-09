N = int(input())
def stori(n):
    if n==0:
        return n
    return n*stori(n-1)
print(stori(N))