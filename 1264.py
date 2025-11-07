letters = ['a','e','i','o','u','A','E','I','O','U']

while True:
    a = int(input())
    if a=='#':
        break
    for i in a:
        for i in letters:
            count+=1
    print(count)