def shellSort(nums):
    n = len(nums)
    gap = n // 2
    gaplist = []
    while gap:
        gaplist.append(gap)
        gap = gap // 2
    for g in gaplist:
        for i in range(g, n):
            j = i
            while j - g >= 0 and nums[j - g] > nums[i]:
                nums[j - g], nums[i] = nums[i], nums[j - g]
                j -= 1
    return nums


res = shellSort([1, 0, 4, -1, 2, 7, 9, 8, 10, 3, 6, 5, 18])
print(res)
