def boss_counters(n, t_in, t_out, m, t_boss):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    for i in range(m):
        events.append((t_boss[i], 0))
    events.sort()
    online = 0
    boss_ans = []
    for event in events:
        if event[1] == -1:
            online += 1
        elif event[1] == 1:
            online -= 1
        else:
            boss_ans.append(online)
    return boss_ans


m = 4
n = 3
t_in = [10, 15, 20]  # time in hours
t_out = [17, 16, 22]
t_boss = [12, 14, 16, 22]
print(boss_counters(n, t_in, t_out, m, t_boss))
