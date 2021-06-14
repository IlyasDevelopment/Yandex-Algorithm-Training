n, k, m = list(map(int, input().split()))
alloy_to_add, cnt = 0, 0
while int(n / k) > 0 and k >= m:
    for i in range(int(n / k)):
        cnt += int(k / m)
        alloy_to_add += k % m
    alloy_to_add += n % k
    n = alloy_to_add
    alloy_to_add = 0
print(cnt)
