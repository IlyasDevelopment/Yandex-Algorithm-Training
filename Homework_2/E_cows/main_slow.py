num = int(input())
seq = list(map(int, input().split()))
variants = []
sorted_seq = sorted(seq, reverse=True)
winner = max(seq)
for i in range(seq.index(max(seq)) + 1, num - 1):
    if (seq[i] - 5) % 10 == 0 and seq[i + 1] < seq[i]:
        if seq[i] == winner:
            variants.append(1)
        else:
            variants.append(sorted_seq.index(seq[i]) + 1) # list.index() has O(n) complexity then this line makes a problem
if not variants:
    print(0)
else:
    print(min(variants))
