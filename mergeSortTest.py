# merge Sort

def subList(list):       # แยกลิสต์
    if(len(list) == 1):
        return list
    mid = len(list)//2          # // หมายถึงไม่เอาเศษ
    leftList = list[:mid]       # :mid หมายถึงครึ่งหน้า
    rightList = list[mid:]      # mid: หมายถึงครึ่งหลัง
    leftList = subList(leftList)
    rightList = subList(rightList)
    return merge(leftList, rightList)

def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])

    """if len(a) == 0:
        c = c + b
    else:
        c = c + a"""

    while len(a) != 0:
        c.append(a[0])
        a.remove(a[0])
    while len(b) != 0:
        c.append(b[0])
        b.remove(b[0])
    return c

list = [56, 8, 10, 7, 16, 25, 99, 48]
print(subList(list))