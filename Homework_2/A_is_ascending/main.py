seq = list(map(int, input().split()))
flag = False
for i in range(1, len(seq)):
    if seq[i - 1] >= seq[i] and not flag:
        print('NO')
        flag = True
if not flag:
    print('YES')
