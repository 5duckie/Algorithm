import math

total = 0

A,B,C = map(int,input().split())
T = int(input())

total = A

if T>30:
    total+=math.ceil((T-30)/B)
    print(math.ceil(total))