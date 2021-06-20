dict_a = {}

with open('input.txt', 'r') as input_file:
    result = []
    for line in input_file.readlines():
        for word in line.split():
            if word not in dict_a:
                dict_a[word] = 0
            else:
                dict_a[word] += 1
            result.append(dict_a[word])

print(' '.join(map(str, result)))
