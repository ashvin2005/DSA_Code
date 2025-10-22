"""
Binary Search Algorithm Implementation
====================================

Algorithm Description:
Binary Search is a highly efficient searching algorithm that works on sorted arrays. 
It follows a divide-and-conquer approach by repeatedly dividing the search interval in half.
If the value of the search key is less than the item in the middle of the interval, 
the search narrows to the lower half. Otherwise, it narrows to the upper half.

Time Complexity: O(log n) - because the search space is halved at each step.
Space Complexity: 
- O(1) for the iterative version.
- O(log n) for the recursive version (due to recursion stack).

Prerequisite: The array must be sorted.

Applications:
- Searching in large sorted datasets (e.g., dictionaries, phone books).
- Finding the insertion point for an element in a sorted array.
- Used as a building block for more complex algorithms.
- Finding the first or last occurrence of an element.
"""

from typing import List, Any, Optional, Callable


def binary_search_iterative(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform binary search iteratively to find the index of a target value.
    
    Args:
        arr (List[Any]): A sorted list of elements.
        target (Any): The value to search for.
    
    Returns:
        Optional[int]: The index of the target if found, otherwise None.
        
    Example:
        >>> binary_search_iterative([2, 5, 7, 8, 11, 12], 11)
        4
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate mid point to avoid potential overflow
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return None  # Target not found


def binary_search_recursive(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform binary search recursively.
    
    Args:
        arr (List[Any]): A sorted list of elements.
        target (Any): The value to search for.
    
    Returns:
        Optional[int]: The index of the target if found, otherwise None.
    """
    return _binary_search_recursive_helper(arr, target, 0, len(arr) - 1)


def _binary_search_recursive_helper(arr: List[Any], target: Any, left: int, right: int) -> Optional[int]:
    """Helper function for recursive binary search."""
    if left > right:
        return None  # Base case: target not found
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return _binary_search_recursive_helper(arr, target, mid + 1, right)
    else:
        return _binary_search_recursive_helper(arr, target, left, mid - 1)


def find_first_occurrence(arr: List[Any], target: Any) -> Optional[int]:
    """
    Find the index of the first occurrence of a target value.
    
    Args:
        arr (List[Any]): A sorted list.
        target (Any): The value to search for.
        
    Returns:
        Optional[int]: Index of the first occurrence, or None if not found.
        
    Example:
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4], 2)
        1
    """
    left, right = 0, len(arr) - 1
    result = None
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result


def find_last_occurrence(arr: List[Any], target: Any) -> Optional[int]:
    """
    Find the index of the last occurrence of a target value.
    
    Args:
        arr (List[Any]): A sorted list.
        target (Any): The value to search for.
        
    Returns:
        Optional[int]: Index of the last occurrence, or None if not found.
        
    Example:
        >>> find_last_occurrence([1, 2, 2, 2, 3, 4], 2)
        3
    """
    left, right = 0, len(arr) - 1
    result = None
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result


def find_insertion_point(arr: List[Any], target: Any) -> int:
    """
    Find the index where a target should be inserted to maintain sort order.
    This is equivalent to bisect_left.
    
    Args:
        arr (List[Any]): A sorted list.
        target (Any): The value to insert.
        
    Returns:
        int: The index where the target should be inserted.
        
    Example:
        >>> find_insertion_point([1, 3, 5, 6], 5)
        2
        >>> find_insertion_point([1, 3, 5, 6], 2)
        1
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left


def test_binary_search():
    """Comprehensive test cases for all binary search functions."""
    print("Testing Binary Search Algorithms")
    print("=" * 50)
    
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # Test 1: Iterative search
    print("\nTest 1: Iterative Search")
    assert binary_search_iterative(arr, 23) == 5, "Iterative: Found failed"
    assert binary_search_iterative(arr, 91) == 9, "Iterative: Last element failed"
    assert binary_search_iterative(arr, 2) == 0, "Iterative: First element failed"
    assert binary_search_iterative(arr, 15) is None, "Iterative: Not found failed"
    print("Iterative search tests passed. ✅")
    
    # Test 2: Recursive search
    print("\nTest 2: Recursive Search")
    assert binary_search_recursive(arr, 23) == 5, "Recursive: Found failed"
    assert binary_search_recursive(arr, 91) == 9, "Recursive: Last element failed"
    assert binary_search_recursive(arr, 2) == 0, "Recursive: First element failed"
    assert binary_search_recursive(arr, 15) is None, "Recursive: Not found failed"
    print("Recursive search tests passed. ✅")
    
    # Test 3: First and Last Occurrence
    print("\nTest 3: First and Last Occurrence")
    dup_arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    assert find_first_occurrence(dup_arr, 2) == 1, "First occurrence of 2 failed"
    assert find_last_occurrence(dup_arr, 2) == 3, "Last occurrence of 2 failed"
    assert find_first_occurrence(dup_arr, 5) == 7, "First occurrence of 5 failed"
    assert find_last_occurrence(dup_arr, 5) == 10, "Last occurrence of 5 failed"
    assert find_first_occurrence(dup_arr, 7) is None, "First occurrence of non-existent failed"
    print("First/Last occurrence tests passed. ✅")
    
    # Test 4: Insertion Point
    print("\nTest 4: Insertion Point")
    ins_arr = [10, 20, 30, 40, 50]
    assert find_insertion_point(ins_arr, 35) == 3, "Insertion point in middle failed"
    assert find_insertion_point(ins_arr, 5) == 0, "Insertion point at start failed"
    assert find_insertion_point(ins_arr, 60) == 5, "Insertion point at end failed"
    assert find_insertion_point(ins_arr, 30) == 2, "Insertion point for existing element failed"
    print("Insertion point tests passed. ✅")
    
    # Test 5: Edge cases
    print("\nTest 5: Edge Cases")
    assert binary_search_iterative([], 5) is None, "Empty array test failed"
    assert binary_search_iterative([5], 5) == 0, "Single element found failed"
    assert binary_search_iterative([5], 1) is None, "Single element not found failed"
    print("Edge case tests passed. ✅")
    
    print("\n" + "=" * 50)
    print("All binary search tests passed! 🎉")


def interactive_demo():
    """Interactive demonstration of binary search."""
    print("\nInteractive Binary Search Demo")
    print("=" * 30)
    
    try:
        user_input = input("Enter a sorted list of numbers (space-separated): ")
        arr = sorted(list(map(int, user_input.split())))
        print(f"Using sorted array: {arr}")
        
        target_input = input("Enter the number to search for: ")
        target = int(target_input)
        
        print("\n--- Results ---")
        
        # Standard search
        index = binary_search_iterative(arr, target)
        if index is not None:
            print(f"Target {target} found at index: {index}")
        else:
            print(f"Target {target} not found in the array.")
        
        # First/Last occurrence
        first = find_first_occurrence(arr, target)
        last = find_last_occurrence(arr, target)
        if first is not None:
            print(f"First occurrence of {target} is at index: {first}")
            print(f"Last occurrence of {target} is at index: {last}")
            count = last - first + 1
            print(f"Total occurrences of {target}: {count}")
        
        # Insertion point
        insertion_point = find_insertion_point(arr, target)
        print(f"To maintain order, {target} should be inserted at index: {insertion_point}")
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Run comprehensive tests
    test_binary_search()
    
    # Run interactive demo
    # Uncomment the line below to try the interactive version
    # interactive_demo()
    
    # Example usage
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Binary Search in Action")
    print("=" * 60)
    
    my_sorted_list = [5, 13, 22, 22, 22, 45, 67, 89, 101]
    search_value = 22
    
    print(f"Array: {my_sorted_list}")
    print(f"Searching for: {search_value}\n")
    
    idx = binary_search_iterative(my_sorted_list, search_value)
    print(f"Standard search found at index: {idx}")
    
    first_idx = find_first_occurrence(my_sorted_list, search_value)
    print(f"First occurrence is at index: {first_idx}")
    
    last_idx = find_last_occurrence(my_sorted_list, search_value)
    print(f"Last occurrence is at index: {last_idx}")
    
    new_val = 50
    insert_idx = find_insertion_point(my_sorted_list, new_val)
    print(f"Insertion point for {new_val} is: {insert_idx}")