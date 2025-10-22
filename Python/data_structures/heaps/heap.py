"""
Heap / Priority Queue Implementation
===================================

Data Structure Description:
A Heap is a specialized tree-based data structure that satisfies the heap property:
- Min Heap: Parent node is always smaller than or equal to its children
- Max Heap: Parent node is always greater than or equal to its children

Heaps are commonly implemented using arrays and are complete binary trees,
making them very efficient for priority queue operations.

Time Complexities:
- Insert: O(log n) - add element and bubble up
- Extract Min/Max: O(log n) - remove root and bubble down
- Get Min/Max: O(1) - peek at root
- Build Heap: O(n) - heapify array
- Heapsort: O(n log n)

Space Complexity: O(n)

Applications:
- Priority Queue implementation
- Heap Sort algorithm
- Finding K largest/smallest elements
- Dijkstra's shortest path algorithm
- Huffman coding (data compression)
- Order statistics (median maintenance)
- Task scheduling in operating systems
"""


class MinHeap:
    """
    Min Heap implementation where parent is smaller than children.
    """
    
    def __init__(self):
        """Initialize an empty min heap."""
        self.heap = []
    
    def parent(self, i):
        """Get parent index."""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index."""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index."""
        return 2 * i + 2
    
    def has_parent(self, i):
        """Check if node has parent."""
        return self.parent(i) >= 0
    
    def has_left_child(self, i):
        """Check if node has left child."""
        return self.left_child(i) < len(self.heap)
    
    def has_right_child(self, i):
        """Check if node has right child."""
        return self.right_child(i) < len(self.heap)
    
    def swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """
        Insert a value into the heap.
        
        Args:
            value: Value to insert
        
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, index):
        """
        Bubble up element at index to maintain heap property.
        
        Args:
            index (int): Index of element to bubble up
        """
        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def extract_min(self):
        """
        Remove and return the minimum element (root).
        
        Returns:
            The minimum element
        
        Raises:
            IndexError: If heap is empty
        
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Cannot extract from empty heap")
        
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self._bubble_down(0)
        
        return min_value
    
    def _bubble_down(self, index):
        """
        Bubble down element at index to maintain heap property.
        
        Args:
            index (int): Index of element to bubble down
        """
        while self.has_left_child(index):
            smaller_child_index = self.left_child(index)
            
            # Find smaller child
            if (self.has_right_child(index) and 
                self.heap[self.right_child(index)] < self.heap[smaller_child_index]):
                smaller_child_index = self.right_child(index)
            
            # If current element is smaller than both children, done
            if self.heap[index] < self.heap[smaller_child_index]:
                break
            
            self.swap(index, smaller_child_index)
            index = smaller_child_index
    
    def peek(self):
        """
        Return the minimum element without removing it.
        
        Returns:
            The minimum element
        
        Raises:
            IndexError: If heap is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty heap")
        return self.heap[0]
    
    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0
    
    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)
    
    def __len__(self):
        """Return the size of the heap."""
        return len(self.heap)
    
    def __str__(self):
        """String representation of the heap."""
        return f"MinHeap({self.heap})"
    
    def __repr__(self):
        """Official string representation."""
        return f"MinHeap({self.heap})"


class MaxHeap:
    """
    Max Heap implementation where parent is greater than children.
    """
    
    def __init__(self):
        """Initialize an empty max heap."""
        self.heap = []
    
    def parent(self, i):
        """Get parent index."""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index."""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index."""
        return 2 * i + 2
    
    def has_parent(self, i):
        """Check if node has parent."""
        return self.parent(i) >= 0
    
    def has_left_child(self, i):
        """Check if node has left child."""
        return self.left_child(i) < len(self.heap)
    
    def has_right_child(self, i):
        """Check if node has right child."""
        return self.right_child(i) < len(self.heap)
    
    def swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """
        Insert a value into the heap.
        
        Args:
            value: Value to insert
        
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, index):
        """Bubble up element at index to maintain heap property."""
        while self.has_parent(index) and self.heap[index] > self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def extract_max(self):
        """
        Remove and return the maximum element (root).
        
        Returns:
            The maximum element
        
        Raises:
            IndexError: If heap is empty
        
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Cannot extract from empty heap")
        
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self._bubble_down(0)
        
        return max_value
    
    def _bubble_down(self, index):
        """Bubble down element at index to maintain heap property."""
        while self.has_left_child(index):
            larger_child_index = self.left_child(index)
            
            # Find larger child
            if (self.has_right_child(index) and 
                self.heap[self.right_child(index)] > self.heap[larger_child_index]):
                larger_child_index = self.right_child(index)
            
            # If current element is larger than both children, done
            if self.heap[index] > self.heap[larger_child_index]:
                break
            
            self.swap(index, larger_child_index)
            index = larger_child_index
    
    def peek(self):
        """Return the maximum element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at empty heap")
        return self.heap[0]
    
    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0
    
    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)
    
    def __len__(self):
        """Return the size of the heap."""
        return len(self.heap)
    
    def __str__(self):
        """String representation of the heap."""
        return f"MaxHeap({self.heap})"


def heapify(arr):
    """
    Convert an array into a min heap in-place.
    
    Args:
        arr (list): Array to heapify
    
    Time Complexity: O(n)
    """
    n = len(arr)
    # Start from last non-leaf node and heapify down
    for i in range(n // 2 - 1, -1, -1):
        _heapify_down(arr, n, i)


def _heapify_down(arr, n, i):
    """Helper function to heapify down from index i."""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        _heapify_down(arr, n, smallest)


def heap_sort(arr):
    """
    Sort an array using heap sort algorithm.
    
    Args:
        arr (list): Array to sort
    
    Returns:
        list: Sorted array
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _max_heapify_down(arr_copy, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
        _max_heapify_down(arr_copy, i, 0)
    
    return arr_copy


def _max_heapify_down(arr, n, i):
    """Helper for max heap bubble down."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _max_heapify_down(arr, n, largest)


def find_k_largest(arr, k):
    """
    Find k largest elements using min heap.
    
    Args:
        arr (list): Input array
        k (int): Number of largest elements to find
    
    Returns:
        list: k largest elements
    
    Time Complexity: O(n log k)
    """
    if k <= 0 or k > len(arr):
        raise ValueError("k must be between 1 and array length")
    
    min_heap = MinHeap()
    
    # Add first k elements
    for i in range(k):
        min_heap.insert(arr[i])
    
    # For remaining elements, if larger than min, replace
    for i in range(k, len(arr)):
        if arr[i] > min_heap.peek():
            min_heap.extract_min()
            min_heap.insert(arr[i])
    
    return min_heap.heap


def find_k_smallest(arr, k):
    """
    Find k smallest elements using max heap.
    
    Args:
        arr (list): Input array
        k (int): Number of smallest elements to find
    
    Returns:
        list: k smallest elements
    
    Time Complexity: O(n log k)
    """
    if k <= 0 or k > len(arr):
        raise ValueError("k must be between 1 and array length")
    
    max_heap = MaxHeap()
    
    # Add first k elements
    for i in range(k):
        max_heap.insert(arr[i])
    
    # For remaining elements, if smaller than max, replace
    for i in range(k, len(arr)):
        if arr[i] < max_heap.peek():
            max_heap.extract_max()
            max_heap.insert(arr[i])
    
    return max_heap.heap


def test_heap():
    """Comprehensive test cases for heap implementations."""
    print("Testing Heap Implementations")
    print("=" * 50)
    
    # Test 1: Min Heap basic operations
    print("\nTest 1: Min Heap Basic Operations")
    min_heap = MinHeap()
    values = [5, 3, 7, 1, 9, 2]
    for val in values:
        min_heap.insert(val)
    print(f"After inserting {values}: {min_heap}")
    
    assert min_heap.peek() == 1, "Min should be 1"
    assert min_heap.extract_min() == 1, "Should extract 1"
    assert min_heap.peek() == 2, "New min should be 2"
    print("Min heap tests passed ✅")
    
    # Test 2: Max Heap basic operations
    print("\nTest 2: Max Heap Basic Operations")
    max_heap = MaxHeap()
    for val in values:
        max_heap.insert(val)
    print(f"After inserting {values}: {max_heap}")
    
    assert max_heap.peek() == 9, "Max should be 9"
    assert max_heap.extract_max() == 9, "Should extract 9"
    assert max_heap.peek() == 7, "New max should be 7"
    print("Max heap tests passed ✅")
    
    # Test 3: Heap Sort
    print("\nTest 3: Heap Sort")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = heap_sort(test_arr)
    print(f"Original: {test_arr}")
    print(f"Sorted:   {sorted_arr}")
    assert sorted_arr == sorted(test_arr), "Heap sort failed"
    print("Heap sort tests passed ✅")
    
    # Test 4: Find k largest
    print("\nTest 4: Find K Largest Elements")
    arr = [7, 10, 4, 3, 20, 15, 8, 2]
    k = 3
    result = find_k_largest(arr, k)
    print(f"Array: {arr}")
    print(f"3 largest: {sorted(result, reverse=True)}")
    assert sorted(result, reverse=True) == [20, 15, 10], "K largest failed"
    print("K largest tests passed ✅")
    
    # Test 5: Find k smallest
    print("\nTest 5: Find K Smallest Elements")
    result = find_k_smallest(arr, k)
    print(f"Array: {arr}")
    print(f"3 smallest: {sorted(result)}")
    assert sorted(result) == [2, 3, 4], "K smallest failed"
    print("K smallest tests passed ✅")
    
    # Test 6: Edge cases
    print("\nTest 6: Edge Cases")
    empty_heap = MinHeap()
    assert empty_heap.is_empty() == True, "Should be empty"
    
    try:
        empty_heap.extract_min()
        assert False, "Should raise exception"
    except IndexError:
        print("Empty heap extract raises exception ✅")
    
    single_heap = MinHeap()
    single_heap.insert(42)
    assert single_heap.peek() == 42, "Single element test failed"
    print("Edge cases passed ✅")
    
    print("\n" + "=" * 50)
    print("All tests passed! 🎉")


if __name__ == "__main__":
    # Run comprehensive tests
    test_heap()
    
    # Demonstrate usage
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Heap Applications")
    print("=" * 60)
    
    # Demo 1: Priority Queue simulation
    print("\n1. Priority Queue (Task Scheduler):")
    task_queue = MinHeap()
    tasks = [(3, "Low priority task"), (1, "High priority task"), (2, "Medium priority task")]
    
    for priority, task in tasks:
        task_queue.insert((priority, task))
        print(f"Added: {task} (priority: {priority})")
    
    print("\nProcessing tasks in priority order:")
    while not task_queue.is_empty():
        priority, task = task_queue.extract_min()
        print(f"Executing: {task} (priority: {priority})")
    
    # Demo 2: Finding top k elements
    print("\n2. Finding Top 3 Scores:")
    scores = [85, 92, 78, 95, 88, 73, 90, 87]
    top_3 = find_k_largest(scores, 3)
    print(f"All scores: {scores}")
    print(f"Top 3 scores: {sorted(top_3, reverse=True)}")