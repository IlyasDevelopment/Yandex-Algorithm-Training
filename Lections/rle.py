def rle(s):
    def pack(s,cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsum = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsum:
            ans.append(pack(lastsum, i - lastpos))
            lastpos = i
            lastsum = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)
