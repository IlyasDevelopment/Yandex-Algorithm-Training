with open('input.txt', 'r') as input_file:
    rows = []
    for seq in input_file.readlines():
        rows.append(set(map(int, seq.split())))

with open('output.txt', 'w') as output_file:
    intersection = set()
    for element in rows[0]:
        if element in rows[1]:
            intersection.add(element)
    output_file.write(' '.join(map(str, sorted(intersection))))
