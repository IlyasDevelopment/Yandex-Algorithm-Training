# O(n) complexity but it is not a good idea to change initial list seq

seq = list(map(int, input().split()))

if len(seq) == 2:
    print(min(seq), max(seq))
else:
    max_positive = max(seq)
    seq.remove(max_positive)
    max_positive2 = max(seq)
    min_negative = min(seq)
    seq.remove(min_negative)
    min_negative2 = min(seq)

    if max_positive * max_positive2 > min_negative * min_negative2:
        print(max_positive2, max_positive)
    else:
        print(min_negative, min_negative2)
