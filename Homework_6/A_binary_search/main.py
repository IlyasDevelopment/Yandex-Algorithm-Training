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
    x, seq = params
    return seq[index] >= x


n, k = map(int, input().split())
first_list = list(map(int, input().split()))
first_list.sort()
second_list = list(map(int, input().split()))

for i in range(k):
    ind = l_bin_search(0, len(first_list) - 1, check_is_g_e, (second_list[i], first_list))
    if first_list[ind] == second_list[i]:
        print('YES')
    else:
        print('NO')
