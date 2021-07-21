def time_with_visitors(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()
    online = 0
    not_empty_time = 0
    for i in range(len(events)):
        if online > 0:
            not_empty_time += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return not_empty_time


n = 3
t_in = [10, 15, 20]  # time in hours
t_out = [17, 16, 22]
print(time_with_visitors(n, t_in, t_out))
