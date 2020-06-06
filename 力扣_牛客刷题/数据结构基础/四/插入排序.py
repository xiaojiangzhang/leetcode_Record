from random import random


def insertSort(nums):
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        nums[j + 1] = temp
    return nums


arr = [int(random() * 10) for _ in range(20)]
print(arr)
res = insertSort(arr)
print(res)
