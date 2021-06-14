values = []
for i in range(3):
    values.append(float(input()))
a, b, c = values
if a == 0 and b < 0:
    ans = 'NO SOLUTION'
elif c < 0:
    ans = 'NO SOLUTION'
elif a == 0 and b >= 0:
    if b == c*c:
        ans = 'MANY SOLUTIONS'
    else:
        ans = 'NO SOLUTION'
else:
    x = (c*c - b) / a
    if x - int(x) == 0:
        ans = int(x)
    else:
        ans = 'NO SOLUTION'
print(ans)
