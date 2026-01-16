# total = ()
# something = 0
multiples = []

n,k = map(int,input().split())
for i in range(1,n+1):
    if n%i==0:
        multiples.append(i)

if len(multiples)>=k:
    print(multiples[k-1])
else:
    print(0)
# for i in range(n):
#     multiple = n%k
#     if n%k==0:
#         total+=i
#     else:
#         pass

# if total==k:
#     total = something
#     print(something)
# else:
#     print(0)
