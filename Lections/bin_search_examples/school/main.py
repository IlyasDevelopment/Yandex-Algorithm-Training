def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_endowment(m, params):
    n, k = params
    # ((k + m)/(n + m)) >= 1/3 but division is not desirable
    return (k + m) * 3 >= n + m


N = 25
K = 3
l = 0
r = N
# how many parents should be
min_k = l_bin_search(l, r, check_endowment, (N, K))
# how may parents we should add
print(min_k - K)
