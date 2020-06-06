from random import random


def bubbleSort(nums):
    n = len(nums)
    flag = True
    for i in range(n):
        if flag:
            for j in range(n - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


arr = [int(random() * 11) for _ in range(11)]
print(arr)
res = bubbleSort(arr)
print(res)
