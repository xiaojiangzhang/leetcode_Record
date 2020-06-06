def deFind(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = int((left + right) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] == target:
            right = mid
    return left


def deFind2(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            left = mid + 1
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    return left-1


res = deFind2([1, 2, 2, 33], 2)
print(res)
