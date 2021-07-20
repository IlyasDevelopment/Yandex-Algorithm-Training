def count_segments_for_dots(events, dots):
    result = [None] * len(dots)
    cnt = 0
    for event in events:
        if event[1] == -1:
            cnt += 1
        elif event[1] == 1:
            cnt -= 1
        else:
            ind = event[2]
            result[ind] = cnt
    return result


n, m = map(int, input().split())
events = []
for i in range(n):
    a, b = map(int, input().split())
    events.append((min(a, b), -1))
    events.append((max(a, b), 1))
dots = list(map(int, input().split()))
for i in range(m):
    events.append((dots[i], 0, i))
events.sort()
# print(events)
print(*count_segments_for_dots(events, dots))
