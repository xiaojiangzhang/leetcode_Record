from random import random


def shellSort(nums):
    n = len(nums)
    gap = n // 2
    gap_list = []
    while gap:
        gap_list.append(gap)
        gap = gap // 2
    for g in gap_list:
        for i in range(g, n):
            j = i
            while j - g >= 0 and nums[j - g] > nums[j]:
                nums[j - g], nums[j] = nums[j], nums[j - g]
                j -= g
    return nums


arr = [int(random() * 11) for _ in range(11)]
print(arr)
res = shellSort(arr)
print(res)
