# Insertion Sort

def InsertionSort(list):
    for i in range(1, len(list)):
        j = i - 1
        temp = list[i]
        while (list[j] > temp) and (j >= 0):    # ถ้าตัวหน้ามากกว่าคัวหลัง และ ตำแหน่งlist >= 0
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp

list = [56, 13, 0, 9, 45, -6]
InsertionSort(list)
print (list)