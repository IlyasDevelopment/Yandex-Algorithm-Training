triangle_sides = []
for i in range(3):
    triangle_sides.append(int(input()))
a, b, c = triangle_sides
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')
