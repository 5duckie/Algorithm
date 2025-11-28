N = int(input())
total = 1
for i in range(1,N+1):
    total*=i

total = str(total)[::-1]
mojang = 0

for i in range(len(total)):
    if int(total[i])==0:
        mojang+=1
    else:
        break

print(mojang)