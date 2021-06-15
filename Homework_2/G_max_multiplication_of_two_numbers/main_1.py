import heapq
from operator import mul


def get_calculate(numbers):
    two_smallest = heapq.nsmallest(2, numbers)
    two_biggest = heapq.nlargest(2, numbers)
    if mul(*two_smallest) > mul(*two_biggest):
        return sorted(two_smallest)
    else:
        return sorted(two_biggest)


seq = list(map(int, input().split()))
print(*get_calculate(seq))
