def selectSort(nums):
    n = len(nums)
    for i in range(n):
        min = nums[i]
        for j in range(i, n):
            if nums[j] < min:
                min, nums[j] = nums[j], min
        nums[i] = min
    return nums


res = selectSort([49, 38, 65, 97, 76, 13, 27, 49])
print(res)
