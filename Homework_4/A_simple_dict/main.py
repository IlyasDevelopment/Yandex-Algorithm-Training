n = int(input())
dict_a, dict_b = {}, {}
for i in range(n):
    first, second = input().split()
    dict_a[first] = second
    dict_b[second] = first
word = input()
if word in dict_a:
    print(dict_a[word])
elif word in dict_b:
    print(dict_b[word])
