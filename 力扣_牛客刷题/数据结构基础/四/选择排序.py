from random import random


def selectSort(nums):
    n = len(nums)
    for i in range(n):
        min = nums[i]
        for j in range(i, n):
            if nums[j] < min:
                nums[j], min = min, nums[j]
        nums[i] = min
    return nums

arr = [int(random() * 10) for _ in range(11)]
print(arr)
res = selectSort(arr)
print(res)
