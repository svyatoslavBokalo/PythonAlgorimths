def BinarySearch(mas, element, startPoint, endPoint, middlePoint):
    # check if such element exist
    if (startPoint > endPoint):
        return -1

    # check that there is no fixation
    if( endPoint- startPoint == 1):
        if(mas[startPoint] == element):
            return startPoint
        elif (mas[endPoint] == element):
            return endPoint
        else:
            return -1

    # check element is equals to the middle element
    if (element == mas[middlePoint]):
        return middlePoint
    else:
        if(element > mas[middlePoint]):
            startPoint = middlePoint
            middlePoint = (endPoint + startPoint)//2
            return BinarySearch(mas, element, startPoint, endPoint, middlePoint)
        else:
            endPoint = middlePoint
            middlePoint = (endPoint + startPoint)//2
            return BinarySearch(mas, element, startPoint, endPoint, middlePoint)


mas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(mas1)

element = 44
middlePoint = (len(mas1) - 1 + 0)//2
index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
print("index = ", index)

mas1 = [3, 6, 8, 12, 14, 15, 16, 19, 22, 23, 24, 29, 33]
print(mas1)
element = 12
middlePoint = (len(mas1) - 1 + 0) // 2
index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
print("index = ", index)
element = 23
middlePoint = (len(mas1) - 1 + 0) // 2
index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
print("index = ", index)
element = 7
middlePoint = (len(mas1) - 1 + 0) // 2
index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
print("index = ", index)