def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_amount(d, params):
    a, b, c = params
    return 2 * (a * 2 + b * 3 + c * 4 + d * 5) >= 7 * (a + b + c + d)


a = int(input())
b = int(input())
c = int(input())
print(l_bin_search(0, 10**16, check_amount, (a, b, c)))
