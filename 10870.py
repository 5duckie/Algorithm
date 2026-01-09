n = int(input())
def fib(N):
    if N==0 or N==1:
        return N
    return fib(N-1)+fib(N-2)
print(fib(n))