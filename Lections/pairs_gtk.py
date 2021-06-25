def cnt_pairs_wirth_diff_g_t_k(sorted_nums, k):
    cnt_pairs = 0
    last = 0
    for first in range(len(sorted_nums)):
        while last < len(sorted_nums) and sorted_nums[last] - sorted_nums[first] <= k:
            last += 1
        cnt_pairs += len(sorted_nums) - last
    return cnt_pairs


print(cnt_pairs_wirth_diff_g_t_k([1, 3, 7, 8], 4))
# O(n) complexity
