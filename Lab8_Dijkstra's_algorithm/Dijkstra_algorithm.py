def read_from_file(fileName = "test_dataset.txt"):
    count = amount_top(fileName)
    the_tops = []
    file = open(fileName, "r")
    lines = file.readlines()
    for line in lines:
        s = line.split()[1:]
        mas = []
        for el in s:
            mas.append(el.split(','))
        # print(mas)
        for i in range(1, count+1):
            mas1 = []
            for el in mas:
                if el[0] == i:
                    mas1.append(el)
                else:
                    mas1.append([i, 0])

            the_tops.append(mas1)

    print(the_tops)
    file.close()
def amount_top(fileName = "test_dataset.txt"):
    file = open(fileName, "r")
    count = len(file.readlines())
    file.close()
    return count


read_from_file()