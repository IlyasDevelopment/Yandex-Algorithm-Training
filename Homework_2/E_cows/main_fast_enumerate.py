# this solution neither better nor worse than main_fast.py
num = int(input())
seq = list(map(int, input().split()))
vasya_place = None
winner = max(seq)
max_place = seq.index(winner)
for place, value in enumerate(seq[max_place + 1: num - 1]):
    if (value % 10 == 5) and (seq[max_place + place + 1] > seq[max_place + place + 2]):
        if vasya_place is None:
            vasya_place = value
        if vasya_place < value:
            vasya_place = value
if vasya_place:
    sorted_seq = sorted(seq, reverse=True)
    print(sorted_seq.index(vasya_place) + 1)
else:
    print(0)
