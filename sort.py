def pivot_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

    # Partition the array into two sub-arrays:
    # 'left' with elements less than the pivot
    # 'right' with elements greater than or equal to the pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively sort the sub-arrays and combine them with the pivot
    return pivot_sort(left) + [pivot] + pivot_sort(right)
