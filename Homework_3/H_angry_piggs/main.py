n = int(input())
dictionary = {}
for i in range(n):
    x, y = map(int, input().split())
    if x not in dictionary:
        dictionary[x] = []
    dictionary[x].append(y)
print(len(dictionary))
