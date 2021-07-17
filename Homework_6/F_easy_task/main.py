def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_time(m, params):
    n, x, y = params
    return (m // x + m // y) >= n - 1


n, x, y = map(int, input().split())
print(min(x, y) + l_bin_search(0, (n - 1)*max(x, y), check_time, (n, x, y)))
