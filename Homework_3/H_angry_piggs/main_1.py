n = int(input())
unique_x_values = set()
for i in range(n):
    x, y = map(int, input().split())
    unique_x_values.add(x)
print(len(unique_x_values))
