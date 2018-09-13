def listsum(list1):
    theSum = 0
    for i in list1:
        theSum = theSum + i
    return theSum


list1 = [{'school_class': '4a', 'scores': [3, 4, 5, 4, 2, 4, 4, 3, 2, 2, 4, 5]},
{'school_class': '5a', 'scores': [2, 5, 4, 3, 3, 2, 5, 4]}]

    print(listsum(list1))