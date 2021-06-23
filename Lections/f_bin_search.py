def dist(t, params):
    x, v = params
    min_pos = max_pos = x[0] + v[0] * t
    for i in range(1, len(x)):
        now_pos = x[i] + v[i] * t
        min_pos = min(max_pos, now_pos)
        max_pos = max(max_pos, now_pos)
    return max_pos - min_pos


def check_asc(t, eps, params):
    return dist(t + eps, params) >= dist(t, params)


def f_bin_search(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if check_asc(m, eps, params):
            r = m
        else:
            l = m
    return l
