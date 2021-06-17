def group_words(words):
    groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    ans = []
    for sorted_word in groups:
        ans.append(groups[sorted_word])
    return ans


print(group_words(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
