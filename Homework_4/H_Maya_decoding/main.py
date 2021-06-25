with open('input.txt', 'r') as input_file:
    g, s_len = map(int, input_file.readline().split())
    w = list(input_file.readline()[:-1])
    s = list(input_file.readline()[:-1])


def make_dict(elements):
    new_dict = {}
    for element in elements:
        if element not in new_dict:
            new_dict[element] = 0
        new_dict[element] += 1
    return new_dict


cnt = 0
w_dict = make_dict(w)
part = s[:g]
s_part_dict = make_dict(part)
if w_dict == s_part_dict:
    cnt += 1
first = part[0]
last = part[g - 1]

for i in range(1, s_len - g + 1):
    s_part_dict[first] -= 1
    if s_part_dict[first] == 0:
        del s_part_dict[first]

    first = s[i]
    last = s[g + i - 1]

    if last not in s_part_dict:
        s_part_dict[last] = 0
    s_part_dict[last] += 1
    
    if w_dict == s_part_dict:
        cnt += 1

print(cnt)
