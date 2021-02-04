def BubbleSort(list):
    for k in range(len(list) - 1, 0, -1):  # เริ่มตั้งแต่ n-1 ถึง 0 ลดลงทีละ 1
        for PTR in range(k):
            if list[PTR] > list[PTR + 1]:  # ถ้าตัวข้างหน้ามากกว่าตัวข้างหลัง
                temp = list[PTR]
                list[PTR] = list[PTR + 1]
                list[PTR + 1] = temp
    print(list)


def InsertionSort(list):
    for i in range(1, len(list)):
        j = i - 1
        temp = list[i]
        while (list[j] > temp) and (j >= 0):    # ถ้าตัวหน้ามากกว่าคัวหลัง และ ตำแหน่งlist >= 0
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp
    print(list)


def SelectionSort(list):
    for j in range(len(list)):
        indexMin = j
        for i in range(j+1, len(list)):
            if list[indexMin] > list[i] :
                indexMin = i
        list[j],list[indexMin] = list[indexMin],list[j]
    print(list)

list = []
n = int(input("input index data : "))
for i in range(n):
    a = int(input("input data : "))
    list.append(a)

print("--------------------------------")
print("Menu")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
choice = int(input("Input Choice : "))
if choice == 1:
    BubbleSort(list)
elif choice == 2:
    InsertionSort(list)
elif choice == 3:
    SelectionSort(list)
else:
    print("Error!!!")