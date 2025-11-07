N = int(input())
cards = set(map(int,input().split()))
    
M = int(input())
numbers = list(map(int,input().split()))

for i in range(len(numbers)):
    num = numbers[i]
    B = {num}
    if len(cards&B)==1:
        print(1)
    else:
        print(0)