seq = []
for i in range(5):
    seq.append(int(input()))
a, b, c, d, e = seq
if (a <= d and b <= e) or (a <= d and c <= e) or (b <= d and c <= e)\
        or (a <= e and b <= d) or (a <= e and c <= d) or (b <= e and c <= d):
    print('YES')
else:
    print('NO')
