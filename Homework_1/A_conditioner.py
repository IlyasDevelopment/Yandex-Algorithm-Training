t_room, t_cond = map(int, input().split())
mode = input()
ans = t_room
if (mode == 'freeze' and t_room > t_cond) or (mode == 'heat' and t_room < t_cond) or (mode == 'auto'):
    ans = t_cond
print(ans)
