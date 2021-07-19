def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l


def check_width(width, params):
    n, m, t = params
    return t >= (2 * m * width) + (2 * (n - 2 * width) * width)


n = int(input())
m = int(input())
t = int(input())
print(r_bin_search(0, min(n, m)//2, check_width, (n, m, t)))
