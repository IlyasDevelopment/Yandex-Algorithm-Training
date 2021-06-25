n = int(input())
dict_lower = {}
for _ in range(n):
    s = input()
    s_lower = s.lower()
    if s_lower not in dict_lower:
        dict_lower[s_lower] = set()
    dict_lower[s_lower].add(s)
text = input()
mistakes = 0
for word in text.split():
    word_lower = word.lower()
    if word_lower in dict_lower:
        if word not in dict_lower[word_lower]:
            mistakes += 1
    else:
        stresses = 0
        for c in word:
            if c.isupper():
                stresses += 1
        if stresses != 1:
            mistakes += 1
print(mistakes)


# пройти по всем словам текста
# если слово из маленьких букв в словаре, то проверить есть ли слово с ударением в множестве
# если слово в множестве, то ошибки нет
# если слово из маленьких букв не в словаре, то проверить, что ровно одно ударение, иначе ошибка
