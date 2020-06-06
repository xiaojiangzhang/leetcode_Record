def Find( target, array):
    # write code here
    if len(array) == 0:
        return False
    clo = len(array[0])-1
    row = 0
    while clo >= 0 and row < len(array):
        if array[row][clo] == target:
            return True
        elif array[row][clo] < target:
            row += 1
        else:
            clo -= 1
    return False

a = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 1
res = Find(target, a)
print(res)
