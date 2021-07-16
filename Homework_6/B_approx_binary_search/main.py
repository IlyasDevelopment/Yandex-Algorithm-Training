def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_is_g(index, params):
    x, seq = params
    return seq[index] > x


n, k = map(int, input().split())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

for i in range(k):
    # next line returns place (index) where current element
    # of the second list may be added to maintain first list sorted
    ind = l_bin_search(0, len(first_list) - 1, check_is_g, (second_list[i], first_list))
    # print('ind:', ind)
    if ind == 0:
        print(first_list[ind])
    elif second_list[i] - first_list[ind - 1] <= first_list[ind] - second_list[i]:
        print(first_list[ind - 1])
    else:
        print(first_list[ind])
