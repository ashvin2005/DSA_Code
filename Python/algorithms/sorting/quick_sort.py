"""
Quick Sort Algorithm Implementation
==================================

Algorithm Description:
Quick Sort is a highly efficient divide-and-conquer sorting algorithm. It works by selecting
a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
according to whether they are less than or greater than the pivot. The sub-arrays are then
sorted recursively.

The algorithm follows these steps:
1. Choose a pivot element (various strategies: first, last, middle, random)
2. Partition: rearrange array so elements smaller than pivot come before, larger come after
3. Recursively apply quick sort to the sub-arrays

Time Complexity: 
- Best/Average: O(n log n)
- Worst: O(n²) - when pivot is always smallest or largest element
Space Complexity: O(log n) for recursion stack

Key Features:
- In-place sorting (doesn't require extra space for arrays)
- Not stable (relative order of equal elements may change)
- Cache-efficient due to locality of reference

Applications:
- Default sorting algorithm in many programming languages
- When average-case performance is critical
- Embedded systems with limited memory
- Real-time systems requiring predictable performance
"""

import random
from typing import List, Any, Callable


def quick_sort(arr: List[Any], key: Callable = None, reverse: bool = False) -> List[Any]:
    """
    Sort an array using the quick sort algorithm.
    
    Args:
        arr (List[Any]): The array to be sorted
        key (Callable, optional): Function to extract comparison key
        reverse (bool): If True, sort in descending order
    
    Returns:
        List[Any]: A new sorted array
    
    Example:
        >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr.copy()
    
    arr_copy = arr.copy()
    _quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1, key, reverse)
    return arr_copy


def _quick_sort_recursive(arr: List[Any], low: int, high: int, 
                          key: Callable, reverse: bool) -> None:
    """
    Recursive helper function for quick sort.
    
    Args:
        arr (List[Any]): Array to sort (modified in place)
        low (int): Starting index
        high (int): Ending index
        key (Callable): Comparison key function
        reverse (bool): Sort order flag
    """
    if low < high:
        # Partition the array and get pivot index
        pivot_index = _partition(arr, low, high, key, reverse)
        
        # Recursively sort elements before and after partition
        _quick_sort_recursive(arr, low, pivot_index - 1, key, reverse)
        _quick_sort_recursive(arr, pivot_index + 1, high, key, reverse)


def _partition(arr: List[Any], low: int, high: int, 
              key: Callable, reverse: bool) -> int:
    """
    Partition the array using the last element as pivot (Lomuto partition scheme).
    
    Args:
        arr (List[Any]): Array to partition
        low (int): Starting index
        high (int): Ending index
        key (Callable): Comparison key function
        reverse (bool): Sort order flag
    
    Returns:
        int: Final position of the pivot element
    """
    pivot = arr[high]
    pivot_key = key(pivot) if key else pivot
    
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        current_key = key(arr[j]) if key else arr[j]
        
        # If current element is smaller/larger than pivot (depending on reverse)
        if (current_key <= pivot_key) != reverse:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_hoare(arr: List[Any]) -> List[Any]:
    """
    Quick sort using Hoare's partition scheme (more efficient).
    
    Args:
        arr (List[Any]): The array to be sorted
    
    Returns:
        List[Any]: A new sorted array
    """
    if len(arr) <= 1:
        return arr.copy()
    
    arr_copy = arr.copy()
    _quick_sort_hoare_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quick_sort_hoare_recursive(arr: List[Any], low: int, high: int) -> None:
    """Recursive helper for Hoare's partition scheme."""
    if low < high:
        pivot_index = _hoare_partition(arr, low, high)
        _quick_sort_hoare_recursive(arr, low, pivot_index)
        _quick_sort_hoare_recursive(arr, pivot_index + 1, high)


def _hoare_partition(arr: List[Any], low: int, high: int) -> int:
    """
    Hoare's partition scheme - more efficient than Lomuto's.
    Uses two pointers moving towards each other.
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Move i right while elements are less than pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Move j left while elements are greater than pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        # If pointers crossed, return j
        if i >= j:
            return j
        
        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_randomized(arr: List[Any]) -> List[Any]:
    """
    Randomized quick sort - chooses random pivot to avoid worst case.
    
    Args:
        arr (List[Any]): The array to be sorted
    
    Returns:
        List[Any]: A new sorted array
    """
    if len(arr) <= 1:
        return arr.copy()
    
    arr_copy = arr.copy()
    _quick_sort_randomized_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quick_sort_randomized_recursive(arr: List[Any], low: int, high: int) -> None:
    """Recursive helper for randomized quick sort."""
    if low < high:
        pivot_index = _randomized_partition(arr, low, high)
        _quick_sort_randomized_recursive(arr, low, pivot_index - 1)
        _quick_sort_randomized_recursive(arr, pivot_index + 1, high)


def _randomized_partition(arr: List[Any], low: int, high: int) -> int:
    """Partition with random pivot selection."""
    # Choose random pivot and swap with last element
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    # Use standard partition
    return _partition(arr, low, high, None, False)


def quick_sort_3way(arr: List[Any]) -> List[Any]:
    """
    3-way quick sort - efficient for arrays with many duplicate elements.
    Partitions array into three parts: < pivot, = pivot, > pivot
    
    Args:
        arr (List[Any]): The array to be sorted
    
    Returns:
        List[Any]: A new sorted array
    """
    if len(arr) <= 1:
        return arr.copy()
    
    arr_copy = arr.copy()
    _quick_sort_3way_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quick_sort_3way_recursive(arr: List[Any], low: int, high: int) -> None:
    """Recursive helper for 3-way quick sort."""
    if low >= high:
        return
    
    lt, gt = _partition_3way(arr, low, high)
    _quick_sort_3way_recursive(arr, low, lt - 1)
    _quick_sort_3way_recursive(arr, gt + 1, high)


def _partition_3way(arr: List[Any], low: int, high: int) -> tuple:
    """
    3-way partition: divides array into < pivot, = pivot, > pivot.
    
    Returns:
        tuple: (lt, gt) where arr[low:lt] < pivot, arr[lt:gt+1] = pivot, arr[gt+1:high+1] > pivot
    """
    pivot = arr[low]
    lt = low  # arr[low:lt] < pivot
    i = low + 1  # arr[lt:i] = pivot
    gt = high  # arr[gt+1:high+1] > pivot
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt


def kth_smallest(arr: List[Any], k: int) -> Any:
    """
    Find the kth smallest element using quick select algorithm.
    
    Args:
        arr (List[Any]): Input array
        k (int): Position (1-indexed)
    
    Returns:
        Any: The kth smallest element
    
    Example:
        >>> kth_smallest([7, 10, 4, 3, 20, 15], 3)
        7
    """
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and array length")
    
    arr_copy = arr.copy()
    return _quick_select(arr_copy, 0, len(arr_copy) - 1, k - 1)


def _quick_select(arr: List[Any], low: int, high: int, k: int) -> Any:
    """Quick select algorithm to find kth smallest element."""
    if low == high:
        return arr[low]
    
    pivot_index = _randomized_partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return _quick_select(arr, low, pivot_index - 1, k)
    else:
        return _quick_select(arr, pivot_index + 1, high, k)


def test_quick_sort():
    """Comprehensive test cases for quick sort implementations."""
    print("Testing Quick Sort Algorithms")
    print("=" * 50)
    
    # Test 1: Basic sorting
    print("\nTest 1: Basic Quick Sort")
    test1 = [64, 34, 25, 12, 22, 11, 90]
    result1 = quick_sort(test1)
    expected1 = [11, 12, 22, 25, 34, 64, 90]
    print(f"Input:    {test1}")
    print(f"Output:   {result1}")
    assert result1 == expected1, "Test 1 failed"
    
    # Test 2: Already sorted
    print("\nTest 2: Already Sorted Array")
    test2 = [1, 2, 3, 4, 5]
    result2 = quick_sort(test2)
    assert result2 == test2, "Test 2 failed"
    print(f"Result: {result2} ✅")
    
    # Test 3: Reverse sorted
    print("\nTest 3: Reverse Sorted Array")
    test3 = [5, 4, 3, 2, 1]
    result3 = quick_sort(test3)
    expected3 = [1, 2, 3, 4, 5]
    assert result3 == expected3, "Test 3 failed"
    print(f"Result: {result3} ✅")
    
    # Test 4: Duplicates (3-way quick sort is optimal)
    print("\nTest 4: Array with Duplicates (3-way)")
    test4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result4 = quick_sort_3way(test4)
    expected4 = sorted(test4)
    assert result4 == expected4, "Test 4 failed"
    print(f"Input:  {test4}")
    print(f"Output: {result4}")
    
    # Test 5: Hoare's partition
    print("\nTest 5: Hoare's Partition Scheme")
    test5 = [10, 7, 8, 9, 1, 5]
    result5 = quick_sort_hoare(test5)
    expected5 = [1, 5, 7, 8, 9, 10]
    assert result5 == expected5, "Test 5 failed"
    print(f"Result: {result5} ✅")
    
    # Test 6: Randomized quick sort
    print("\nTest 6: Randomized Quick Sort")
    test6 = [random.randint(1, 100) for _ in range(20)]
    result6 = quick_sort_randomized(test6)
    expected6 = sorted(test6)
    assert result6 == expected6, "Test 6 failed"
    print(f"Sorted 20 random elements ✅")
    
    # Test 7: Kth smallest element
    print("\nTest 7: Kth Smallest Element")
    test7 = [7, 10, 4, 3, 20, 15]
    k = 3
    result7 = kth_smallest(test7, k)
    expected7 = 7
    print(f"Array: {test7}")
    print(f"3rd smallest: {result7}")
    assert result7 == expected7, "Test 7 failed"
    
    # Test 8: Edge cases
    print("\nTest 8: Edge Cases")
    assert quick_sort([]) == [], "Empty array failed"
    assert quick_sort([42]) == [42], "Single element failed"
    assert quick_sort([2, 1]) == [1, 2], "Two elements failed"
    print("All edge cases passed ✅")
    
    # Test 9: Custom key function
    print("\nTest 9: Sorting with Custom Key")
    words = ['banana', 'pie', 'Washington', 'book']
    result9 = quick_sort(words, key=len)
    expected9 = ['pie', 'book', 'banana', 'Washington']
    print(f"Sort by length: {result9}")
    assert result9 == expected9, "Test 9 failed"
    
    # Test 10: Reverse order
    print("\nTest 10: Reverse Order Sorting")
    test10 = [1, 3, 2, 5, 4]
    result10 = quick_sort(test10, reverse=True)
    expected10 = [5, 4, 3, 2, 1]
    assert result10 == expected10, "Test 10 failed"
    print(f"Result: {result10} ✅")
    
    print("\n" + "=" * 50)
    print("All tests passed! 🎉")


if __name__ == "__main__":
    # Run comprehensive tests
    test_quick_sort()
    
    # Demonstrate different variants
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Quick Sort Variants")
    print("=" * 60)
    
    demo_array = [33, 10, 59, 27, 41, 18, 44]
    print(f"Original array: {demo_array}\n")
    
    print(f"Standard Quick Sort:    {quick_sort(demo_array)}")
    print(f"Hoare's Partition:      {quick_sort_hoare(demo_array)}")
    print(f"Randomized Quick Sort:  {quick_sort_randomized(demo_array)}")
    print(f"3-Way Quick Sort:       {quick_sort_3way(demo_array)}")
    
    # Demonstrate kth smallest
    print(f"\nFinding 4th smallest element: {kth_smallest(demo_array, 4)}")