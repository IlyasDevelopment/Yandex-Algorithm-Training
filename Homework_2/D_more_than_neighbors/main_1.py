seq = list(map(int, input().split()))
ans = 0
for i in range(1, len(seq) - 1):
    if seq[i - 1] < seq[i] > seq[i + 1]:
        ans += 1
print(ans)
