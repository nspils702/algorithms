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
def quick_sort(nums, low, high):
    if low < high:
        nums, p = partition(nums, low, high)
        nums = quick_sort(nums, low, p - 1)
        nums = quick_sort(nums, p + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return nums, i

            
# chooses pivot
# puts all code on left of pivot
# inserts pivot



def test():
    list = [55, 33, 22, 11, 33, 44, 55, 66, 77]
    start = time.time()
    print(quick_sort(list, 0, len(list)-1))
    end = time.time()
    print(start-end)

test()