s = input()
ans = ''
anscnt = 0
dict = {}
for now in s:
    if now not in dict:
        dict[now] = 0
    dict[now] += 1
for key in dict:
    if dict[key] > anscnt:
        anscnt = dict[key]
    ans = key
print(ans)
