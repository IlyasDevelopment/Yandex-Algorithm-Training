def easypeasy(s):
    lastsum = s[0]
    ans = []
    for i in range(len(s)):
        if s[i] != lastsum:
            ans.append(lastsum)
            lastsum = s[i]
    ans.append(lastsum)
    return ''.join(ans)
