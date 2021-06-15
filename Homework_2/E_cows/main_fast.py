num = int(input())
seq = list(map(int, input().split()))
vasya_values = []
winner = max(seq)
for i in range(seq.index(max(seq)) + 1, num - 1):
    if (seq[i] - 5) % 10 == 0 and seq[i] > seq[i + 1]:
            vasya_values.append(seq[i])
if not vasya_values:
    print(0)
else:
    sorted_seq = sorted(seq, reverse=True)
    print(sorted_seq.index(max(vasya_values)) + 1)
