"""
Kadane's Algorithm - Maximum Subarray Sum
==========================================

Algorithm Description:
Kadane's algorithm is a dynamic programming approach to find the maximum sum of a contiguous subarray 
within a one-dimensional array of numbers. It efficiently solves the maximum subarray problem in O(n) time.

The key insight is that at each position, we decide whether to:
1. Start a new subarray from current element
2. Extend the existing subarray by including current element

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using constant extra space

Applications:
- Stock trading (maximum profit in consecutive days)
- Image processing (finding brightest region)
- Bioinformatics (finding significant DNA sequences)
"""

def kadanes_algorithm(arr):
    """
    Find the maximum sum of contiguous subarray using Kadane's algorithm.
    
    Args:
        arr (list): List of integers (can contain negative numbers)
    
    Returns:
        tuple: (max_sum, start_index, end_index) where:
               - max_sum: Maximum sum found
               - start_index: Starting index of the maximum subarray
               - end_index: Ending index of the maximum subarray
    
    Raises:
        ValueError: If array is empty
    
    Example:
        >>> kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        (6, 3, 6)  # subarray [4, -1, 2, 1] has sum 6
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    # Initialize variables
    max_sum = arr[0]  # Maximum sum found so far
    current_sum = arr[0]  # Sum of current subarray
    
    # Track indices for the maximum subarray
    start = 0  # Start of maximum subarray
    end = 0    # End of maximum subarray
    temp_start = 0  # Temporary start for current subarray
    
    # Iterate through array starting from second element
    for i in range(1, len(arr)):
        # If current sum becomes negative, start new subarray
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            # Extend current subarray
            current_sum += arr[i]
        
        # Update maximum if current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end


def kadanes_all_negative(arr):
    """
    Modified Kadane's algorithm that handles the case when all elements are negative.
    In such cases, returns the least negative element.
    
    Args:
        arr (list): List of integers
    
    Returns:
        tuple: (max_sum, start_index, end_index)
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    # Check if all elements are negative
    if all(x < 0 for x in arr):
        max_element = max(arr)
        max_index = arr.index(max_element)
        return max_element, max_index, max_index
    
    return kadanes_algorithm(arr)


def print_subarray_details(arr, max_sum, start, end):
    """
    Helper function to print detailed results of Kadane's algorithm.
    
    Args:
        arr (list): Original array
        max_sum (int): Maximum sum found
        start (int): Start index of maximum subarray
        end (int): End index of maximum subarray
    """
    subarray = arr[start:end+1]
    print(f"Original Array: {arr}")
    print(f"Maximum Sum: {max_sum}")
    print(f"Maximum Subarray: {subarray}")
    print(f"Indices: [{start}, {end}]")
    print(f"Length: {end - start + 1}")


# Test cases and examples
def test_kadanes_algorithm():
    """
    Comprehensive test cases for Kadane's algorithm implementation.
    """
    print("Testing Kadane's Algorithm")
    print("=" * 50)
    
    # Test Case 1: Mixed positive and negative numbers
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = kadanes_algorithm(test1)
    print("\nTest Case 1: Mixed array")
    print_subarray_details(test1, *result1)
    assert result1[0] == 6, "Test 1 failed"
    
    # Test Case 2: All positive numbers
    test2 = [1, 2, 3, 4, 5]
    result2 = kadanes_algorithm(test2)
    print("\nTest Case 2: All positive")
    print_subarray_details(test2, *result2)
    assert result2[0] == 15, "Test 2 failed"
    
    # Test Case 3: All negative numbers
    test3 = [-5, -2, -8, -1, -4]
    result3 = kadanes_all_negative(test3)
    print("\nTest Case 3: All negative")
    print_subarray_details(test3, *result3)
    assert result3[0] == -1, "Test 3 failed"
    
    # Test Case 4: Single element
    test4 = [42]
    result4 = kadanes_algorithm(test4)
    print("\nTest Case 4: Single element")
    print_subarray_details(test4, *result4)
    assert result4[0] == 42, "Test 4 failed"
    
    # Test Case 5: Alternating positive and negative
    test5 = [5, -3, 5, -3, 5]
    result5 = kadanes_algorithm(test5)
    print("\nTest Case 5: Alternating signs")
    print_subarray_details(test5, *result5)
    assert result5[0] == 9, "Test 5 failed"
    
    # Test Case 6: Large negative in middle
    test6 = [1, 2, -10, 3, 4]
    result6 = kadanes_algorithm(test6)
    print("\nTest Case 6: Large negative in middle")
    print_subarray_details(test6, *result6)
    assert result6[0] == 7, "Test 6 failed"
    
    print("\n" + "=" * 50)
    print("All test cases passed! ✅")


def interactive_demo():
    """
    Interactive demonstration of Kadane's algorithm.
    """
    print("\nInteractive Kadane's Algorithm Demo")
    print("=" * 40)
    
    while True:
        try:
            user_input = input("\nEnter array elements (space-separated integers) or 'quit' to exit: ")
            
            if user_input.lower() == 'quit':
                break
                
            arr = list(map(int, user_input.split()))
            
            if not arr:
                print("Please enter at least one number.")
                continue
            
            result = kadanes_all_negative(arr)
            print("\nResult:")
            print_subarray_details(arr, *result)
            
        except ValueError:
            print("Please enter valid integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Run comprehensive tests
    test_kadanes_algorithm()
    
    # Optional: Run interactive demo
    # Uncomment the line below to try the interactive version
    # interactive_demo()
    
    # Example usage
    print("\nExample Usage:")
    print("-" * 20)
    example_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start_idx, end_idx = kadanes_algorithm(example_array)
    print(f"Array: {example_array}")
    print(f"Maximum subarray sum: {max_sum}")
    print(f"Subarray: {example_array[start_idx:end_idx+1]}")