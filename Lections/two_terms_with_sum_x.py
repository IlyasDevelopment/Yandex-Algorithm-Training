def twotermswithsumx(nums, x):
    prevnums = set()
    for nownum in nums:
        if x -nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0


numbers = [1, 3, 5, 8, 2]
y = 7
print(twotermswithsumx(numbers, y))
