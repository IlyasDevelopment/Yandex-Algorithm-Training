def is_symmetric(nums):
    for i in range(len(nums) // 2):
        if nums[i] != nums[-i - 1]:
            return False
    return True


def symmetric_sequence(nums):
    for i in range(len(nums)):
        if is_symmetric(nums[i:]):
            return list(reversed(nums[:i]))


n = int(input())
nums = list(map(int, input().split()))
result = symmetric_sequence(nums)
print(len(result))
if len(result):
    print(' '.join(map(str, result)))
