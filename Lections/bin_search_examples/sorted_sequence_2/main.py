def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l



def check_is_g_e(index, params):
    seq, x = params
    return seq[index] >= x


def check_is_g(index, params):
    seq, x = params
    return seq[index] > x


seq = [1, 3, 5, 5, 6, 7, 8]
x = 5
l = 0
r = len(seq) - 1
first_index = l_bin_search(l, r, check_is_g_e, (seq, x))
second_index = l_bin_search(l, r, check_is_g, (seq, x))
print(second_index - first_index)
