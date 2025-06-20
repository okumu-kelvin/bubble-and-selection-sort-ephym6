from bubble_sort import bubble_sort

def test_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    # return array to be sorted using bubble_sort
    return [1, 2, 3]

def test_reverse():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    # return array to be sorted using bubble_sort
    return [3, 2, 1]

def test_duplicates():
    assert bubble_sort([4, 5, 3, 4]) == [3, 4, 4, 5]
    # return array to be sorted using bubble_sort
    return [4, 5, 3, 4]

# Implement tests
print("Sorted (using test_sorted()): ", bubble_sort(test_reverse()))
print("Sorted (using test_reverse()): ", bubble_sort(test_reverse()))
print("Sorted (using test_sorted()): ", bubble_sort(test_duplicates()))
