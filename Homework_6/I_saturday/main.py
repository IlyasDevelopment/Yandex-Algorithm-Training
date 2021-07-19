def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_distance(distance, params):
    minbrigades, c, heights = params
    i = 0
    brigades = 0
    while i < len(heights) - c + 1:
        if heights[i + c - 1] - heights[i] <= distance:
            brigades += 1
            i += c
        else:
            i += 1
    return brigades >= minbrigades


n, r, c = map(int, input().split())
heights = []
for _ in range(n):
    heights.append(int(input()))
heights.sort()
print(l_bin_search(0, heights[-1] - heights[0], check_distance, (r, c, heights)))
