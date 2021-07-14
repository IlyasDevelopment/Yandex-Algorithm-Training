def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_problem_count(days, params):
    n, k = params
    return (k + (k + days - 1)) * days // 2 >= n


N = 160
K = 7
l = 0
r = N
print(l_bin_search(l, r, check_problem_count, (N, K)))
