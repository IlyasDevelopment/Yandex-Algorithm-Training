a = int(input())
b = int(input())
n = int(input())
m = int(input())
min_a = n + (n - 1) * a
max_a = n + (n + 1) * a
int_a = list(range(min_a, max_a + 1))
min_b = m + (m - 1) * b
max_b = m + (m + 1) * b
int_b = list(range(min_b, max_b + 1))
intersection = [x for x in int_a if x in int_b]
if not intersection:
    print(-1)
else:
    print(min(intersection), max(intersection))
