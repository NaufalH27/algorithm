

testCase = [2, 3, 20, 4, 6, 2, 1, 4, 693, 31, 4, 4]
target = 31

def sequentialSearch(array : list, target : int)-> int:
    for i, number in enumerate(array):
        if number == target:
            return i
    return -1


print(sequentialSearch(testCase,target))


    