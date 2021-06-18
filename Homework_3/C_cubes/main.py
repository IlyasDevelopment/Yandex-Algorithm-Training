def read_cubes(k):
    new_set = set()
    for i in range(k):
        new_set.add(int(input()))
    return new_set


def difference_between_sets(a, b):
    return sorted(a - b)


def make_print(a):
    print(len(a))
    print(*a)


n, m = map(int, input().split())

ann_cubes = read_cubes(n)
boris_cubes = read_cubes(m)

common_cubes = sorted(set(ann_cubes) & set(boris_cubes))
make_print(common_cubes)

ann_unique_cubes = difference_between_sets(ann_cubes, boris_cubes)
make_print(ann_unique_cubes)

boris_unique_cubes = difference_between_sets(boris_cubes, ann_cubes)
make_print(boris_unique_cubes)
