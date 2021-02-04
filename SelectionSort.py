# Selection Sort
def Min(list):
    indexMin = 0
    for i in range(1, len(list)):
        if list[indexMin] > list[i]:
            indexMin = i
    print(list[indexMin])

def SelectionSort(list):
    for j in range(len(list)):
        indexMin = j
        for i in range(j+1, len(list)):
            if list[indexMin] > list[i] :
                indexMin = i
        list[j],list[indexMin] = list[indexMin],list[j]
    print(list)

list = [33, 12, 1, 10, -8, -56]
SelectionSort(list)

"""list1 = []
a = int(input("input data : "))
list1.append(a)"""