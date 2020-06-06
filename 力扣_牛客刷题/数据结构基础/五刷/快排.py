from random import random


def quickSort(nums, low, high):
    i = low
    j = high
    if i >= j:
        return nums
    temp = nums[i]
    while i < j:
        while i < j and nums[j] >= temp:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= temp:
            i += 1
        nums[j] = nums[i]
    nums[i] = temp
    quickSort(nums, low, i - 1)
    quickSort(nums, i + 1, high)
    return nums


arr = [int(random() * 11) for _ in range(11)]
print(arr)
res = quickSort(arr, 0, len(arr) - 1)
print(res)
