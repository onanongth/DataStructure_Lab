# Bubble Sort

def BubbleSort(list):
    for k in range(len(list) - 1, 0, -1):  # เริ่มตั้งแต่ n-1 ถึง 0 ลดลงทีละ 1
        for PTR in range(k):
            if list[PTR] > list[PTR + 1]:  # ถ้าตัวข้างหน้ามากกว่าตัวข้างหลัง
                temp = list[PTR]
                list[PTR] = list[PTR + 1]
                list[PTR + 1] = temp

list = [6, 23, 14, 8, 10]

# call Function
print(len(list))
BubbleSort(list)
print(list)


"""print (len(list))
for k in range(len(list)-1, 0, -1):     # เริ่มตั้งแต่ n-1 ถึง 0 ลดลงทีละ 1
    for PTR in range (k):
        if list[PTR] > list[PTR + 1]:   # ถ้าตัวข้างหน้ามากกว่าตัวข้างหลัง
            temp = list[PTR]
            list[PTR] = list[PTR + 1]
            list[PTR + 1] = temp"""