def insertSort(nums):
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
    return nums


res = insertSort([49, 38, 65, 97, 76, 13, 27, 49])
print(res)
