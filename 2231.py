total = 0
bunhaehap = 0 
check = False
if check == False:
    print(0)

n=int(input())
for number in range(1,n): # brute force
    temp=str(number)
    sum=number
    for i in temp:
        sum+=int(i)
    if sum == n:
        check = True
        print(number)
        break