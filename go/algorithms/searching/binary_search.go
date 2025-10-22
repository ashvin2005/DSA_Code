/*
Binary Search Implementation in Go
==================================

Algorithm Description:
Binary Search is an efficient searching algorithm that works on sorted arrays.
It repeatedly divides the search interval in half, comparing the target value
with the middle element.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive

Applications:
- Searching in sorted databases
- Finding insertion positions
- Debugging (finding first bad version)
- Game development (AI decision trees)
*/

package main

import (
	"fmt"
	"sort"
)

// BinarySearchIterative searches for target in a sorted slice using iteration
// Returns the index of target if found, -1 otherwise
func BinarySearchIterative(arr []int, target int) int {
	left, right := 0, len(arr)-1

	for left <= right {
		mid := left + (right-left)/2 // Avoid potential overflow

		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1 // Target not found
}

// BinarySearchRecursive searches for target using recursion
func BinarySearchRecursive(arr []int, target int) int {
	return binarySearchRecursiveHelper(arr, target, 0, len(arr)-1)
}

// Helper function for recursive binary search
func binarySearchRecursiveHelper(arr []int, target, left, right int) int {
	if left > right {
		return -1
	}

	mid := left + (right-left)/2

	if arr[mid] == target {
		return mid
	} else if arr[mid] < target {
		return binarySearchRecursiveHelper(arr, target, mid+1, right)
	} else {
		return binarySearchRecursiveHelper(arr, target, left, mid-1)
	}
}

// FindFirstOccurrence finds the first occurrence of target in a sorted array with duplicates
func FindFirstOccurrence(arr []int, target int) int {
	left, right := 0, len(arr)-1
	result := -1

	for left <= right {
		mid := left + (right-left)/2

		if arr[mid] == target {
			result = mid
			right = mid - 1 // Continue searching in left half
		} else if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return result
}

// FindLastOccurrence finds the last occurrence of target in a sorted array with duplicates
func FindLastOccurrence(arr []int, target int) int {
	left, right := 0, len(arr)-1
	result := -1

	for left <= right {
		mid := left + (right-left)/2

		if arr[mid] == target {
			result = mid
			left = mid + 1 // Continue searching in right half
		} else if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return result
}

// FindInsertionPoint finds the index where target should be inserted to maintain sorted order
func FindInsertionPoint(arr []int, target int) int {
	left, right := 0, len(arr)

	for left < right {
		mid := left + (right-left)/2

		if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}

// CountOccurrences counts the number of occurrences of target in sorted array
func CountOccurrences(arr []int, target int) int {
	first := FindFirstOccurrence(arr, target)
	if first == -1 {
		return 0
	}

	last := FindLastOccurrence(arr, target)
	return last - first + 1
}

// SearchInRotatedArray searches in a rotated sorted array
// Example: [4,5,6,7,0,1,2] is rotated from [0,1,2,4,5,6,7]
func SearchInRotatedArray(arr []int, target int) int {
	left, right := 0, len(arr)-1

	for left <= right {
		mid := left + (right-left)/2

		if arr[mid] == target {
			return mid
		}

		// Determine which half is sorted
		if arr[left] <= arr[mid] {
			// Left half is sorted
			if target >= arr[left] && target < arr[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else {
			// Right half is sorted
			if target > arr[mid] && target <= arr[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	return -1
}

// TestBinarySearch runs comprehensive tests
func TestBinarySearch() {
	fmt.Println("Testing Binary Search Implementations")
	fmt.Println("=" + string(make([]byte, 49)))

	// Test 1: Iterative search
	fmt.Println("\nTest 1: Iterative Binary Search")
	arr1 := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	target1 := 23
	result1 := BinarySearchIterative(arr1, target1)
	fmt.Printf("Array: %v\n", arr1)
	fmt.Printf("Searching for %d: found at index %d\n", target1, result1)
	if result1 != 5 {
		panic("Test 1 failed: expected index 5")
	}
	fmt.Println("Test passed ✓")

	// Test 2: Recursive search
	fmt.Println("\nTest 2: Recursive Binary Search")
	result2 := BinarySearchRecursive(arr1, target1)
	fmt.Printf("Recursive search for %d: found at index %d\n", target1, result2)
	if result2 != 5 {
		panic("Test 2 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 3: First and last occurrence
	fmt.Println("\nTest 3: First and Last Occurrence")
	arr3 := []int{1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6}
	target3 := 5
	first := FindFirstOccurrence(arr3, target3)
	last := FindLastOccurrence(arr3, target3)
	count := CountOccurrences(arr3, target3)
	fmt.Printf("Array: %v\n", arr3)
	fmt.Printf("First occurrence of %d: index %d\n", target3, first)
	fmt.Printf("Last occurrence of %d: index %d\n", target3, last)
	fmt.Printf("Total occurrences: %d\n", count)
	if first != 7 || last != 10 || count != 4 {
		panic("Test 3 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 4: Insertion point
	fmt.Println("\nTest 4: Insertion Point")
	arr4 := []int{10, 20, 30, 40, 50}
	target4 := 35
	insertPos := FindInsertionPoint(arr4, target4)
	fmt.Printf("Array: %v\n", arr4)
	fmt.Printf("Insertion point for %d: index %d\n", target4, insertPos)
	if insertPos != 3 {
		panic("Test 4 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 5: Rotated array search
	fmt.Println("\nTest 5: Search in Rotated Array")
	arr5 := []int{4, 5, 6, 7, 0, 1, 2}
	target5 := 0
	result5 := SearchInRotatedArray(arr5, target5)
	fmt.Printf("Rotated array: %v\n", arr5)
	fmt.Printf("Searching for %d: found at index %d\n", target5, result5)
	if result5 != 4 {
		panic("Test 5 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 6: Not found
	fmt.Println("\nTest 6: Target Not Found")
	result6 := BinarySearchIterative(arr1, 100)
	fmt.Printf("Searching for 100: %d (should be -1)\n", result6)
	if result6 != -1 {
		panic("Test 6 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 7: Edge cases
	fmt.Println("\nTest 7: Edge Cases")
	emptyArr := []int{}
	singleArr := []int{42}

	emptyResult := BinarySearchIterative(emptyArr, 5)
	singleResult := BinarySearchIterative(singleArr, 42)

	fmt.Printf("Empty array search: %d (should be -1)\n", emptyResult)
	fmt.Printf("Single element search: %d (should be 0)\n", singleResult)

	if emptyResult != -1 || singleResult != 0 {
		panic("Test 7 failed")
	}
	fmt.Println("Test passed ✓")

	fmt.Println("\n" + string(make([]byte, 50)))
	fmt.Println("All tests passed! 🎉")
}

// Demonstration of practical applications
func DemoBinarySearch() {
	fmt.Println("\n" + string(make([]byte, 60)))
	fmt.Println("DEMONSTRATION: Binary Search Applications")
	fmt.Println(string(make([]byte, 60)))

	// Demo 1: Searching in a sorted list
	fmt.Println("\n1. Searching in a Sorted Database:")
	studentIDs := []int{101, 105, 110, 115, 120, 125, 130, 135, 140}
	searchID := 120

	fmt.Printf("Student IDs: %v\n", studentIDs)
	fmt.Printf("Searching for ID %d...\n", searchID)

	index := BinarySearchIterative(studentIDs, searchID)
	if index != -1 {
		fmt.Printf("✓ Student found at position %d\n", index)
	} else {
		fmt.Println("✗ Student not found")
	}

	// Demo 2: Finding position for new element
	fmt.Println("\n2. Inserting New Element in Sorted Order:")
	scores := []int{65, 72, 78, 85, 92, 95}
	newScore := 80

	fmt.Printf("Existing scores: %v\n", scores)
	fmt.Printf("New score to insert: %d\n", newScore)

	pos := FindInsertionPoint(scores, newScore)
	fmt.Printf("Insert at position %d to maintain order\n", pos)

	// Demo 3: Count occurrences
	fmt.Println("\n3. Counting Duplicate Values:")
	grades := []int{85, 85, 85, 90, 90, 95, 95, 95, 95}
	targetGrade := 95

	fmt.Printf("Grades: %v\n", grades)
	fmt.Printf("Counting occurrences of %d...\n", targetGrade)

	count := CountOccurrences(grades, targetGrade)
	fmt.Printf("Number of students with grade %d: %d\n", targetGrade, count)

	// Demo 4: Using Go's built-in binary search
	fmt.Println("\n4. Using Go's sort.Search (Built-in):")
	numbers := []int{10, 20, 30, 40, 50, 60, 70, 80, 90}
	target := 50

	fmt.Printf("Numbers: %v\n", numbers)
	fmt.Printf("Searching for %d using sort.Search...\n", target)

	idx := sort.Search(len(numbers), func(i int) bool {
		return numbers[i] >= target
	})

	if idx < len(numbers) && numbers[idx] == target {
		fmt.Printf("✓ Found at index %d\n", idx)
	} else {
		fmt.Println("✗ Not found")
	}
}

func main() {
	// Run tests
	TestBinarySearch()

	// Run demonstrations
	DemoBinarySearch()
}
