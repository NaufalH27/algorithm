
#test case array need to be sorted
testCase = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
target = 12


def binarySearch(sortedArray : list, target : int) -> int:
    left : int = 0;
    right : int = len(sortedArray) - 1
    
    while(left <= right):    
        mid : int = left + (right - left) // 2
        
        if(sortedArray[mid] == target):
            return mid
        elif(sortedArray[mid] < target):
            left = mid+1;
        elif(sortedArray[mid] > target):
            right = mid - 1;
    
    return -1


print(binarySearch(testCase, target))