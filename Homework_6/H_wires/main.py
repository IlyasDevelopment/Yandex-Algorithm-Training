def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l


def check_length(length, params):
    k, values = params
    cnt = 0
    for i in range(len(values)):
        cnt += values[i] // length
    return cnt >= k


n, k = map(int, input().split())
values = []
for i in range(n):
    values.append(int(input()))
print(r_bin_search(0, 10**10, check_length, (k, values)))
