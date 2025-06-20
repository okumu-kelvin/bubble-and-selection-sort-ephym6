def selection_sort(arr):
    # TODO: Implement selection sort

    n = len(arr)
    for i in range(n):
        # Minimum element
        min_element = i
        # Find index of minimum element in unsorted array
        for j in range(i+1, n):
            if arr[min_element] > arr[j]:
                min_element = j

        # Implement selection sort by swapping the new minimum element with first element of unsorted array
        arr[i], arr[min_element] = arr[min_element], arr[i]

    return arr
    # pass

#Example
sample_list = [10, 5, 2, 3, 1, 100]
print("Unsorted list: ", sample_list)
#Implement selection sort
print("Sorted list: ", selection_sort(sample_list))
