def get_languages(m):
    languages = set()
    for i in range(m):
        languages.add(input())
    return languages


n = int(input())
all_languages = set()
common_languages = set()
for i in range(n):
    m = int(input())
    new_languages = get_languages(m)
    all_languages |= new_languages
    if i == 0:
        common_languages = new_languages
    common_languages &= new_languages

print(len(common_languages))
print('\n'.join(common_languages))
print(len(all_languages))
print('\n'.join(all_languages))
