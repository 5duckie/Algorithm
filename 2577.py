a = [0,0,0,0,0,0,0,0,0,0]
python_is_good_is_bad = []

A = int(input())
B = int(input())
C = int(input())

python_is_good_is_bad.append(A*B*C)
python_is_good_is_bad = A*B*C
python_is_good_is_bad = str(python_is_good_is_bad)

for i in range(len(python_is_good_is_bad)):
    a[int(python_is_good_is_bad[i])]+=1

print('\n'.join(map(str,a)))