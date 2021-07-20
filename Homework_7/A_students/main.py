def count_cheaters(events):
    cheaters, cnt, a_table, b_table = 0, 0, 0, 0
    for event in events:
        if event[1] == 0:
            cnt += 1
            if cnt == 1:
                a_table = event[0]
        elif event[1] == 1:
            cnt -= 1
            if cnt == 0:
                b_table = event[0]
                cheaters += b_table - a_table + 1
    return cheaters


students, teachers = map(int, input().split())
events = []
for i in range(teachers):
    b, e = map(int, input().split())
    events.append((b, 0))
    events.append((e, 1))
# print(events)
events.sort()
# print(events)
print(students - count_cheaters(events))
