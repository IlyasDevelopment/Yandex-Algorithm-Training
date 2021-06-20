dict_a = {}

with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        for word in line.split():
            if word not in dict_a:
                dict_a[word] = 0
            dict_a[word] += 1


def get_the_most_frequent_words(dictionary):
    words = []
    current_max = 0
    for key, value in dictionary.items():
        if dictionary[key] > current_max:
            current_max = value
    for key, value in dictionary.items():
        if dictionary[key] == current_max:
            words.append(key)
    return words


print(min(get_the_most_frequent_words(dict_a)))

# print(max(dict_a, key=dict_a.get)) prints key with maximum value in dict
# print(max(dict_a, key=lambda x: x[1])) prints the same thing
