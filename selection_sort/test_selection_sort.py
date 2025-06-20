from selection_sort import selection_sort

def test_sorted():
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    # return first array
    return [1, 2, 3]

def test_reverse():
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    # return first array
    return [3, 2, 1]

def test_duplicates():
    assert selection_sort([29, 10, 14, 37, 14]) == [10, 14, 14, 29, 37]
    # return first array
    return [29, 10, 14, 37, 14]

# Test selection sort algorithm using above functions
print("Sorted (using test_sorted()): ", selection_sort(test_sorted()))
print("Sorted (using test_reverse()): ", selection_sort(test_reverse()))
print("Sorted (using test_duplicates()): ", selection_sort(test_duplicates()))