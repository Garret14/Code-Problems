import statistics


def runningmedian(array):
    checkarray = []
    count = 0
    while count != len(array):
        checkarray.append(array[count])
        print(statistics.median(checkarray))
        count += 1

a = [15,6,7,25,7,8]
runningmedian(a)