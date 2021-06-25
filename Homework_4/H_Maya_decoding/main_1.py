def make_dict(s):
    s_dict = {}
    for c in s:
        if c not in s_dict:
            s_dict[c] = 0
        s_dict[c] += 1
    return s_dict


def match_dicts(dict1, dict2):
    matches = 0
    for c in dict1:
        if c in dict2 and dict1[c] == dict2[c]:
            matches += 1
    return matches


def modify_dict(s_dict, w_dict, symbol, count_modifier):
    ans = 0
    if symbol not in s_dict:
        s_dict[symbol] = 0
    if symbol in w_dict and s_dict[symbol] == w_dict[symbol]:
        ans -= 1
    s_dict[symbol] += count_modifier
    if symbol in w_dict and s_dict[symbol] == w_dict[symbol]:
        ans = 1
    return ans


with open('input.txt', 'r') as input_file:
    len_w, len_s = map(int, input_file.readline().split())
    w = input_file.readline()[:-1]
    s = input_file.readline()[:-1]


w_dict = make_dict(w)
s_dict = make_dict(s[:len_w])
matching_letters = match_dicts(w_dict, s_dict)
occurences = 0
if matching_letters == len(w_dict):
    occurences += 1
for i in range(len_w, len_s):
    matching_letters += modify_dict(s_dict, w_dict, s[i - len_w], -1)
    matching_letters += modify_dict(s_dict, w_dict, s[i], +1)
    if matching_letters == len(w_dict):
        occurences += 1
print(occurences)

# works with PyPy
