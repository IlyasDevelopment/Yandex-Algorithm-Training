def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_board(size, params):
    w, h, n = params
    return (size // w) * (size // h) >= n


w, h, n = map(int, input().split())
print(l_bin_search(0, 40000*10**9, check_board, (w, h, n)))
