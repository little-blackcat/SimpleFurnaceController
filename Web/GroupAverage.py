

def groupAndAverage(listToGroup, listToAverage):

    elemInGroupNum = 0
    elemInGroupSum = 0

    groupLabels = []
    averageInGroup = []

    previousElem = listToGroup[0]

    iterator = iter(listToAverage)

    for elem in listToGroup:
        if previousElem != elem:
            average = float(elemInGroupSum) / float(elemInGroupNum)

            averageInGroup.append(average)
            groupLabels.append(previousElem)

            elemInGroupSum = 0
            elemInGroupNum = 0

        elemInGroupSum = elemInGroupSum + next(iterator)
        elemInGroupNum += 1
        previousElem = elem

    # post factum
    average = float(elemInGroupSum) / float(elemInGroupNum)
    averageInGroup.append(average)
    groupLabels.append(previousElem)

    return groupLabels, averageInGroup



