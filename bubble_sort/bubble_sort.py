def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort

    # START: Traversing through all elements in array
    for i in range(len(unsorted_list)):
        # Inner loop compares adjacent elements
        for j in range(len(unsorted_list)-1):
            # Swap if element after is less than the previous element
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list
    # pass

# Sample array
sample_list = [10, 5, 2, 3, 1, 100]
print("Unsorted list: ", sample_list)

#Bubble sorted list
print("Bubble sorted list: ", bubble_sort(sample_list))
