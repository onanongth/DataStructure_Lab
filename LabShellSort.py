def shellSort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list), 1):
            temp = list[i]
            subI = i
            while subI >= gap and list[subI - gap] > temp:
                list[subI] = list[subI - gap]
                subI = subI - gap
            list[subI] = temp
        gap = gap // 2
    return list

list = [65, 4, 80, 7, 10, 34, 10]
print(shellSort(list))