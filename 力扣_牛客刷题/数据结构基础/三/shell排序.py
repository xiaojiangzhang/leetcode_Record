def shellSort(nums):
    n = len(nums)
    gap = n // 2
    gap_list = []
    while gap:
        gap_list.append(gap)
        gap = gap // 2
    for g in gap_list:
        for i in range(g, n):
            while i - g >= 0 and nums[i - g] > nums[i]:
                nums[i - g], nums[i] = nums[i], nums[i - g]
                i -= g
    return nums


res = shellSort([49, 38, 65, 97, 76, 13, 27, 49])
print(res)
