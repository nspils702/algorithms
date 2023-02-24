import time
        
def bubble_sort(arr):
        swapping = True
        while swapping:
            swapping = False
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    swapping = True
        return arr

#merge_sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    median = len(arr) // 2
    left = merge_sort(arr[:median])
    right = merge_sort(arr[median:])
    return merge(left, right)

def merge(left, right):
    arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    arr += left[i:]
    arr += right[j:]
    return arr
###

#quick_sort
def quick_sort(arr, low, high):
    while low < high:
        arr, p = partition(arr, low, high)
        arr = quick_sort(arr, low, p-1)
        arr = quick_sort(arr, p+1, high)
    return arr
    
def partition(arr, low, high):
    p = arr[high]
    index = low
    for j in range(low, high):
        if arr[j] < p:
            arr[index], arr[j] = arr[j], arr[index]
            index += 1
    arr[index], arr[high] = arr[high], arr[index]
    return arr, p

            
# chooses pivot
# puts all code on left of pivot
# inserts pivot



def test():
    list = [55, 33, 22, 11, 33, 44, 55, 66, 77]
    start = time.time()
    print(quick_sort(list, 0, len(list)))
    end = time.time()
    print(start-end)

test()