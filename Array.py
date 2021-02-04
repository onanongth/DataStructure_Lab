from array import*
data = array('i',[])
top = 0

while True :
    print('Menu')
    print(' 1:put')
    print(' 2:pop')
    print(' 3:exit')
    choice = input(' input your choice : ')
    choice = int(choice)

    if choice == 1:             # put
        data1 = input(' input data : ')
        data1 = int(data1)      # data1 = ตัวที่รับเข้ามา
        data.insert(top,data1)
        print('data in stack')
        for x in data:
            print(x)
        print()
        top = top + 1

    elif choice == 2:           # pop
        data.remove(data1)
        print('data in stack')
        top = top - 1            # top = ตำแหน่ง
        for x in data:
            print(x)
        print()

    else:
        print('data in stack')
        for x in data:
            print(x)
        break
