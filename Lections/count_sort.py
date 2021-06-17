def count_sort(seq):
    min_val = min(seq)
    max_val = max(seq)
    k = (max_val - min_val + 1)
    count = [0] * k
    for now in seq:
        count[now - min_val] += 1
    now_pos = 0
    for val in range(0, k):
        for i in range(count[val]):
            seq[now_pos] = val + min_val
            now_pos += 1


grades = [5, 4, 3, 4, 1, 2, 5]
count_sort(grades)
print(grades)
