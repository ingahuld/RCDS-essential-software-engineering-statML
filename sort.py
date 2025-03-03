def pivot_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage:
if __name__ == "__main__":
    sample_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = pivot_sort(sample_list)
    print("Sorted list:", sorted_list)