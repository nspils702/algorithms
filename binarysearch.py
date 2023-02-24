#basic algoirthm
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        elif taget < arr[mid]:
            high = mid - 1
        
    return -1

#algorithm with constraint that must return first index

def binary_search2(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        result = check_solution(arr, target, median)
        if result == 'left':
            high = median -1
        elif result == 'right':
            low = median + 1
        elif result == 'found':
            return median
    return -1

def check_solution(arr, target, median):
    if arr[median] == target:
        if median-1 >= 0 and arr[median -1] == target:
            return 'left'
        else:
            return 'found'
    elif arr[median] < target:
        return 'left'
    else:
        return 'right'

def test():
    print(binary_search2([1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,6,7,8,9,10], 5))

test()