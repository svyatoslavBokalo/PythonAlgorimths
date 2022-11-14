
def BinarySearch(mas, element, startPoint, endPoint, middlePoint):
    # print("startPoint = ", startPoint)
    # print("endPoint = ", endPoint)
    if (startPoint > endPoint):
        return -1

    if( endPoint- startPoint == 1):
        if(mas[startPoint] == element):
            return startPoint
        elif (mas[endPoint] == element):
            return endPoint
        else:
            return -1
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
