def print_chart(s):
    sum_count = {}
    max_sum_count = 0
    for sum in s:
        if sum not in sum_count:
            sum_count[sum] = 0
        sum_count[sum] += 1
        max_sum_count = max(max_sum_count, sum_count[sum])
    sorted_uniq_sums = sorted(sum_count.keys())
    for row in range(max_sum_count, 0, -1):
        for sum in sorted_uniq_sums:
            if sum_count[sum] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_uniq_sums))

# print function is slow, then for efficiency we could save #_rows in list
# and print them once at the end, but in this case complexity is O(n^2)
# so this function is already for small inputs and there is no such need in speed

print_chart('Hello, world!')
