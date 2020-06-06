def bubbleSort(nums):
    n = len(nums)
    flag = True
    for i in range(n):
        if flag:
            flag = False
            for j in range(n - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    flag = True
    return nums


res = bubbleSort([49, 38, 65, 97, 76, 13, 27, 49])
print(res)
