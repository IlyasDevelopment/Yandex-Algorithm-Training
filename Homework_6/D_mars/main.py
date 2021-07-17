def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l



def check_protection(value, params):
    n, a, b, w, h = params
    return n <= (w // (a + 2 * value)) * (h // (b + 2 * value))


n, a, b, w, h = map(int, input().split())
r1 = r_bin_search(0, 10**20, check_protection, (n, a, b, w, h))
r2 = r_bin_search(0, 10**20, check_protection, (n, b, a, w, h))
print(max(r1, r2))
