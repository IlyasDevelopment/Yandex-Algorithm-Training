def wordsindict(dictionary, text):
    goodwords = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])
    print('goodwords:', goodwords)
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans


# complexity O(n*k^2 + m)
dict = {}
dict['abcd'] = 4
dict['eft'] = 2
print('set(dict) -> initial goodwords:', set(dict))
for word in dict:
    print(word)
print(wordsindict(dict, ['abcd', 'its', 'me']))
