num = int(input())
seq = list(map(int, input().split()))
a = int(input())
for i in range(len(seq)):
    if i == 0:
        min_s = abs(a - seq[i])
        ans = seq[i]
    elif abs(a - seq[i]) < min_s:
        min_s = abs(a - seq[i])
        ans = seq[i]
print(ans)
