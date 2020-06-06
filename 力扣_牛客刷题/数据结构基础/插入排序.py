def insertSort(list):
    n = len(list)
    for i in range(1, n):
        # 去出待放入有序列表的第一个元素
        temp = list[i]
        # 获取已排序列表的最后一个元素
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list


res = insertSort([49, 38, 65, 97, 76, 13, 27, 49])
print(res)
