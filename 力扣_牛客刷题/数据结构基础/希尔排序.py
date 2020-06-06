def shellSort(nums):
    n = len(nums)
    gap = n // 2
    gaplist = []
    while gap > 0:
        gaplist.append(gap)
        gap = gap // 2
    for g in gaplist:
        for i in range(g, n):
            j = i
            while j - g >= 0 and nums[j - g] > nums[j]:
                nums[j - g], nums[j] = nums[j], nums[j - g]
                j -= g
    return nums


res = shellSort([1, 0, 4, -1, 2, 7, 9, 8, 10, 3, 6, 5, 18])
print(res)
