import sys


unique_words = set()
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    for word in line.split():
        unique_words.add(word)

print(len(unique_words))

# contest accepts solution even without lines 6-7
