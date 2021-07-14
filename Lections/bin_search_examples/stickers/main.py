def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l


def check_stickers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n


N = 14  # stickers
W = 100
H = 60
l = 0
r = H  # could be r = W as well
print(r_bin_search(l, r, check_stickers, (N, W, H)))
