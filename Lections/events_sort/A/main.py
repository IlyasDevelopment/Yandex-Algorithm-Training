def max_visitors_online(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        elif event[1] == 1:
            online -= 1
        max_online = max(online, max_online)
    return max_online


n = 3
t_in = [10, 15, 20]  # time in hours
t_out = [17, 16, 22]
print(max_visitors_online(n, t_in, t_out))
