numbers = []
for i in range(4):
    numbers.append(list(input()))
    for j in range(len(numbers[i])):
        if numbers[i][j] < '0' or numbers[i][j] > '9':
            numbers[i][j] = ''
    numbers[i] = ''.join(numbers[i])
    if len(numbers[i]) == 7:
        numbers[i] = '8495' + numbers[i]
    if numbers[i][0] == '7':
        numbers[i] = '8' + numbers[i][1:]
for i in range(3):
    if numbers[0] == numbers[i + 1]:
        print('YES')
    else:
        print('NO')
