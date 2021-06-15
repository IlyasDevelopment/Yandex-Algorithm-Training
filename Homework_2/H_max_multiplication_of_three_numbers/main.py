import heapq


def multiply_list(numbers):
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    return result


def get_calculate(numbers):
    two_smallest = heapq.nsmallest(2, numbers)
    three_biggest = heapq.nlargest(3, numbers)
    maximum = max(seq)
    if multiply_list(two_smallest) * maximum > multiply_list(three_biggest):
        return [two_smallest[0], two_smallest[1], maximum]
    else:
        return three_biggest


seq = list(map(int, input().split()))
print(*get_calculate(seq))
