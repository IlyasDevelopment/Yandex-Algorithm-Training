n = int(input())
bricks = {}
for i in range(n):
    width, height = map(int, input().split())
    if width not in bricks:
        bricks[width] = height
    elif height > bricks[width]:
        bricks[width] = height

pyramid_height = 0
for key, value in bricks.items():
    pyramid_height += value
print(pyramid_height)
