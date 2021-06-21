n = int(input())
available_keystrokes = {}
durability = list(map(int, input().split()))
for i in range(n):
    available_keystrokes[i+1] = durability[i]

k = int(input())
keystrokes = list(map(int, input().split()))
for i in range(k):
    available_keystrokes[keystrokes[i]] -= 1

for key, value in available_keystrokes.items():
    if value < 0:
        print('YES')
    else:
        print('NO')
