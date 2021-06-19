genome_a = input()
genome_b = input()

pairs_b = []
for i in range(len(genome_b) - 1):
    pairs_b.append(genome_b[i] + genome_b[i+1])

result = 0
for i in range(len(genome_a) - 1):
    if genome_a[i:i + 2] in pairs_b:
        result += 1

print(result)
