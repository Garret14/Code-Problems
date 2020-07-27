import math


def twosum(array, target):
    check = array[0]
    returnnums = [0,0]
    index = 0
    index2 = 1
    while index != len(array) - 1:
        if index2 == len(array):
            index += 1
            index2 = index + 1
            check = array[index]
        elif check + array[index2] == target:
            returnnums[0] = index
            returnnums[1] = index2
            return returnnums
        else:
            index2 += 1

a = [2,7,11,15]
print(twosum(a,9))
print(twosum(a,26))
print(twosum(a,17))
print(twosum(a,18))
print(twosum(a,20))
