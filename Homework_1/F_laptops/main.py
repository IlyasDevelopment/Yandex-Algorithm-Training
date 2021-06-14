seq = list(map(int, input().split()))

len_a, width_a = max(seq[:2]), min(seq[:2])
len_b, width_b = max(seq[2:]), min(seq[2:])

min_table_length = max(len_a, len_b)
min_table_width = max(width_a, width_b)

width_extension = min(len_a, len_b) - min_table_width
if width_extension < 0:
    width_extension = 0
len_table1 = min_table_length + min(width_a, width_b)
width_table1 = min_table_width + width_extension
table1 = len_table1 * width_table1

length_extension = min(len_a, len_b) - min_table_length
if length_extension < 0:
    length_extension = 0
len_table2 = min_table_width + min(width_a, width_b)
width_table2 = min_table_length + length_extension
table2 = len_table2 * width_table2

if table2 < table1:
    print(len_table2, width_table2)
else:
    print(len_table1, width_table1)
