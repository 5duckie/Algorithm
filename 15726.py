A,B,C = map(int,input().split())

if int(A/B*C) > int(A*B/C):
    print(int(A/B*C))
else:
    print(int(A*B/C))